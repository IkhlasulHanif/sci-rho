import os
import glob
import argparse
import pandas as pd
import torch
import gc
from PIL import Image
from transformers import AutoProcessor, AutoModelForImageTextToText
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser(description="Generate timeseries IAR for a specific problem instance.")
    
    # Core Hyperparameters
    parser.add_argument("--model_name", type=str, required=True, help="Hugging Face model path (e.g., Qwen/Qwen-VL-Chat)")
    parser.add_argument("--subject", type=str, required=True, help="Subject folder (e.g., mathematics)")
    parser.add_argument("--instance", type=str, default="00", help="Instance number folder (e.g., 00)")
    parser.add_argument("--problem_id", type=str, default="all", help="Specific problem ID (e.g., Mat001) or 'all'")
    parser.add_argument("--target_layer", type=int, default=-1, help="Which attention layer to inspect (default: -1 for last layer)")
    
    return parser.parse_args()

def main():
    args = parse_args()
    
    # 1. Setup paths
    raw_data_dir = os.path.join("result", "raw", args.subject, args.instance)
    out_dir = os.path.join("result", "attention_timeseries", args.model_name.replace("/", "_"), args.subject, args.instance)
    os.makedirs(out_dir, exist_ok=True)
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[INFO] Using device: {device} | Target Layer: {args.target_layer}")

    # =========================================================================
    # NEW: Load User Prompt Template
    # =========================================================================
    USER_PROMPT_PATH = "user_prompt.txt"
    user_prompt_template = ""
    if os.path.exists(USER_PROMPT_PATH):
        with open(USER_PROMPT_PATH, "r", encoding="utf-8") as f:
            user_prompt_template = f.read().strip()
        print(f"[INFO] Loaded additional prompt template from {USER_PROMPT_PATH}")
    else:
        print(f"[WARNING] {USER_PROMPT_PATH} not found. Proceeding without template.")

    # 2. Load Model & Processor
    print(f"[INFO] Loading model: {args.model_name}")
    processor = AutoProcessor.from_pretrained(args.model_name)
    model = AutoModelForImageTextToText.from_pretrained(
        args.model_name, 
        dtype=torch.bfloat16, 
        device_map="auto",
        attn_implementation="eager", # Required to output attention weights!
        trust_remote_code=True,
    )
    
    try:
        image_pad_id = processor.tokenizer.convert_tokens_to_ids("<|image_pad|>")
    except:
        image_pad_id = None
        print("[ERROR] Could not find <|image_pad|> token ID.")
        exit()

    # 3. Find the Excel file
    safe_model_filename = args.model_name.replace("/", "_").replace(".", "_") + ".xlsx"
    excel_path = os.path.join(raw_data_dir, safe_model_filename)
    
    if not os.path.exists(excel_path):
        print(f"[ERROR] Excel file not found: {excel_path}")
        return

    df = pd.read_excel(excel_path)
    
    # Filter by problem_id if requested
    if args.problem_id != "all":
        df = df[df['id'] == args.problem_id]
        if df.empty:
            print(f"[ERROR] Problem ID {args.problem_id} not found in {excel_path}")
            return

    # Identify description/response pairs
    desc_cols = [c for c in df.columns if c.startswith("description")]

    # 4. Processing Loop
    tqdm.write(f"\n[INFO] Starting processing for {len(df)} problems...")
    for _, row in tqdm(df.iterrows(), total=len(df), desc="Problems"):
        problem_id = row.get("id", "unknown")
        
        image_path = os.path.join("sample", args.instance, args.subject, str(row["image"]).replace("\\", os.sep))
        try:
            raw_image = Image.open(image_path).convert("RGB")
        except Exception as e:
            tqdm.write(f"[ERROR] Could not load image {image_path}: {e}")
            continue

        for desc_col in tqdm(desc_cols, desc=f"Variants ({problem_id})", leave=False):
            variant = desc_col.replace("description_", "") if desc_col != "description" else "english"
            response_col = desc_col.replace("description", "response")
            
            if response_col not in row or pd.isna(row[response_col]):
                continue
                
            desc_text = str(row[desc_col])
            response_text = str(row[response_col])
            
            # =========================================================================
            # NEW: Stitching logic incorporating the user_prompt_template
            # =========================================================================
            final_text = f"{desc_text}\n\n{user_prompt_template}" if user_prompt_template else desc_text
            
            messages = [
                {"role": "user", "content": [{"type": "image"}, {"type": "text", "text": final_text}]},
                {"role": "assistant", "content": response_text}
            ]
            
            stitched_text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
            
            # Tokenize and process image inputs
            inputs = processor(
                images=raw_image, 
                text=stitched_text, 
                return_tensors="pt"
            ).to(device)
            
            tqdm.write(f"\n[DEBUG - {problem_id} {variant}] inputs.input_ids shape: {inputs.input_ids.shape}")
            if "attention_mask" in inputs:
                tqdm.write(f"[DEBUG - {problem_id} {variant}] inputs.attention_mask shape: {inputs.attention_mask.shape}")
            if "pixel_values" in inputs:
                tqdm.write(f"[DEBUG - {problem_id} {variant}] inputs.pixel_values shape: {inputs.pixel_values.shape}")
            
            with torch.no_grad():
                # Dynamically pass all tensors generated by the processor (handles mm_token_type_ids)
                forward_kwargs = {key: value for key, value in inputs.items()}
                
                # Add our interpretability flag
                forward_kwargs["output_attentions"] = True
                
                outputs = model(**forward_kwargs)
            
            tqdm.write(f"[DEBUG - {problem_id} {variant}] Total attention layers: {len(outputs.attentions)}")
            tqdm.write(f"[DEBUG - {problem_id} {variant}] Raw Target Layer Attention shape: {outputs.attentions[args.target_layer].shape}")
            
            mean_attn = torch.mean(outputs.attentions[args.target_layer][0], dim=0)
            
            tqdm.write(f"[DEBUG - {problem_id} {variant}] mean_attn shape (averaged heads): {mean_attn.shape}")
            
            input_ids_1d = inputs.input_ids[0]
            seq_len = len(input_ids_1d)
            
            # Define basic masks
            is_image_token = (input_ids_1d == image_pad_id)
            
            assistant_token_id = processor.tokenizer.convert_tokens_to_ids("assistant")
            try:
                assistant_start_idx = (input_ids_1d == assistant_token_id).nonzero(as_tuple=True)[0][-1].item()
            except:
                tqdm.write(f"  [WARNING] Could not find assistant start for {variant}. Skipping.")
                continue

            # =========================================================================
            # NEW: Advanced Masking to Fix Bias & Sinks
            # =========================================================================
            # 1. Start with everything before the assistant
            is_prompt_token = torch.arange(seq_len, device=device) < assistant_start_idx
            
            # 2. Fix Attention Sink: Force the first 3 tokens to be False
            # Models dump unused attention here. We don't want it polluting A_text.
            is_prompt_token[:3] = False 
            
            # 3. Fix System Prompt Bias: Exclude the `user_prompt_template`
            if user_prompt_template:
                # Estimate how many tokens the user_prompt_template consumes.
                # We tokenize it alone to get a rough length.
                template_tokens = processor.tokenizer(f"\n\n{user_prompt_template}", return_tensors="pt", add_special_tokens=False).input_ids[0]
                num_template_tokens = len(template_tokens)
                
                # The template sits right before the assistant starts.
                # We add a buffer of +5 tokens to account for ChatML boilerplate 
                # (like <|im_end|>\n<|im_start|>assistant).
                template_start_idx = max(3, assistant_start_idx - num_template_tokens - 5)
                
                # Turn off the text mask for the system template section
                is_prompt_token[template_start_idx:assistant_start_idx] = False
            
            # 4. Finalize text mask (exclude image tokens from the remaining prompt)
            is_text_token = is_prompt_token & ~is_image_token

            tqdm.write(f"[DEBUG - {problem_id} {variant}] is_text_token mask shape: {is_text_token.shape}")
            
            # Count the total valid tokens for length-normalization
            N_image = is_image_token.sum().item()
            N_text = is_text_token.sum().item()
            
            tqdm.write(f"[DEBUG - {problem_id} {variant}] Valid Image Tokens (N_image): {N_image} | Valid Text Tokens (N_text): {N_text}")

            # 5. Extract Timeseries Data
            timeseries_data = []
            token_counter = 1
            
            for gen_idx in range(assistant_start_idx + 1, seq_len):
                gen_token_id = input_ids_1d[gen_idx]
                gen_token_str = processor.tokenizer.decode([gen_token_id])
                
                attn_row = mean_attn[gen_idx - 1, :]
                
                if gen_idx == assistant_start_idx + 1:
                    tqdm.write(f"[DEBUG - {problem_id} {variant}] First attn_row shape: {attn_row.shape}")
                
                # Raw sums
                A_image_raw = attn_row[is_image_token].sum().item()
                A_text_raw = attn_row[is_text_token].sum().item()
                
                # =========================================================================
                # NEW: Mean-Normalized Math
                # =========================================================================
                # Divide the total attention by the length of the modality sequence
                A_image_mean = A_image_raw / N_image if N_image > 0 else 0.0
                A_text_mean = A_text_raw / N_text if N_text > 0 else 0.0
                
                # Calculate the relative focus ratio using the length-normalized values
                IAR_norm = A_image_mean / (A_image_mean + A_text_mean) if (A_image_mean + A_text_mean) > 0 else 0.0
                
                timeseries_data.append({
                    "token_number_generated": token_counter,
                    "token_text": gen_token_str,
                    "IAR_normalized": round(IAR_norm, 4),    # Primary fair metric
                    "A_image_mean": round(A_image_mean, 6),  # Track normalized attention
                    "A_text_mean": round(A_text_mean, 6),    # Track normalized attention
                    "A_image_raw_sum": round(A_image_raw, 4), # Kept for sanity-check debugging
                    "A_text_raw_sum": round(A_text_raw, 4)    # Kept for sanity-check debugging
                })
                token_counter += 1
                
            # 6. Save to CSV
            if timeseries_data:
                csv_filename = f"{problem_id}_{variant}_layer{args.target_layer}.csv"
                csv_path = os.path.join(out_dir, csv_filename)
                pd.DataFrame(timeseries_data).to_csv(csv_path, index=False)
            
            # =========================================================================
            # NEW: RUTHLESS VRAM CLEANUP
            # =========================================================================
            # Delete the massive PyTorch objects holding the attention matrices
            del outputs
            del inputs
            del mean_attn
            del stitched_text
            del messages
            
            # Force Python to run garbage collection immediately
            gc.collect()
            
            # Force PyTorch to flush the VRAM cache before the next loop
            torch.cuda.empty_cache()

    # Cleanup memory before finishing
    del model
    del processor
    torch.cuda.empty_cache()

if __name__ == "__main__":
    main()