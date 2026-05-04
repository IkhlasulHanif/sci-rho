import os
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
    parser.add_argument("--subject", type=str, default="all", help="Subject folder (e.g., mathematics) or 'all'")
    parser.add_argument("--instance", type=str, default="00", help="Instance number folder (e.g., 00)")
    parser.add_argument("--problem_id", type=str, default="all", help="Specific problem ID (e.g., Mat001) or 'all'")
    parser.add_argument("--target_layer", type=int, default=-1, help="Which attention layer to inspect (default: -1 for last layer)")
    
    return parser.parse_args()

def main():
    args = parse_args()
    
    if args.subject.lower() == "all":
        subjects_to_process = ["mathematics", "physics", "chemistry", "biology", "compsci"]
        print(f"[INFO] Subject set to 'all'. Will process: {subjects_to_process}")
    else:
        # If the user typed a specific subject, just put it in a list of 1 item
        subjects_to_process = [args.subject]
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[INFO] Using device: {device} | Target Layer: {args.target_layer}")

    # =========================================================================
    # Load User Prompt Template
    # =========================================================================
    USER_PROMPT_PATH = "user_prompt.txt"
    user_prompt_template = ""
    if os.path.exists(USER_PROMPT_PATH):
        with open(USER_PROMPT_PATH, "r", encoding="utf-8") as f:
            user_prompt_template = f.read().strip()
        print(f"[INFO] Loaded additional prompt template from {USER_PROMPT_PATH}")
    else:
        print(f"[WARNING] {USER_PROMPT_PATH} not found.")
        exit()

    # =========================================================================
    # Load Model & Processor
    # =========================================================================
    print(f"[INFO] Loading model: {args.model_name}")
    processor = AutoProcessor.from_pretrained(args.model_name, trust_remote_code=True)
    model = AutoModelForImageTextToText.from_pretrained(
        args.model_name, 
        dtype=torch.bfloat16, 
        device_map="auto",
        attn_implementation="eager", # Required to output attention weights
        trust_remote_code=True,
    ).eval()

    for current_subject in subjects_to_process:
        # =========================================================================
        # Initialize Debug Log File
        # =========================================================================
        debug_log_path = "tensor_debug_shapes.txt"
        with open(debug_log_path, "w") as f:
            f.write("=== TENSOR SHAPES DEBUG LOG ===\n")
        print(f"\n{'='*60}")
        print(f"[INFO] STARTING SUBJECT: {current_subject.upper()}")
        print(f"{'='*60}")
        
        # 1. Setup paths for THIS specific subject
        raw_data_dir = os.path.join("result", "raw", current_subject, args.instance)
        out_dir = os.path.join("result", "attention_timeseries", args.model_name.replace("/", "_"), current_subject, args.instance)
        os.makedirs(out_dir, exist_ok=True)

        # 2. Find the Excel file
        safe_model_filename = args.model_name.replace("/", "_").replace(".", "_") + ".xlsx"
        excel_path = os.path.join(raw_data_dir, safe_model_filename)
        
        if not os.path.exists(excel_path):
            print(f"[ERROR] Excel file not found for {current_subject}: {excel_path}. Skipping.")
            continue

        df = pd.read_excel(excel_path)
        
        # Filter by problem_id if requested
        if args.problem_id != "all":
            df = df[df['id'] == args.problem_id]
            if df.empty:
                print(f"[ERROR] Problem ID {args.problem_id} not found in {excel_path}")
                continue

        # Identify description/response pairs
        desc_cols = [c for c in df.columns if c.startswith("description")]

        # 4. Processing Loop
        tqdm.write(f"\n[INFO] Starting processing for {len(df)} problems in {current_subject}...")
        for _, row in tqdm(df.iterrows(), total=len(df), desc=f"Problems ({current_subject})"):
            problem_id = row.get("id", "unknown")
            
            image_path = os.path.join("sample", args.instance, current_subject, str(row["image"]).replace("\\", os.sep))
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
                
                # Stitching logic incorporating the user_prompt_template
                final_text = f"{desc_text}\n\n{user_prompt_template}" if user_prompt_template else desc_text
                
                messages = [
                    {"role": "user", "content": [{"type": "image"}, {"type": "text", "text": final_text}]},
                    {"role": "assistant", "content": response_text}
                ]
                
                stitched_text = processor.apply_chat_template(messages, tokenize=False)
                
                # Tokenize and process full inputs natively
                inputs = processor(
                    images=raw_image, 
                    text=stitched_text, 
                    return_tensors="pt"
                ).to(device)
                
                # Write input shapes to log file
                with open(debug_log_path, "a") as f:
                    f.write(f"\n[DEBUG - {problem_id} {variant}]\n")
                    f.write(f"  inputs.input_ids shape: {inputs.input_ids.shape} -> [batch_size, sequence_length]\n")
                    if "attention_mask" in inputs:
                        f.write(f"  inputs.attention_mask shape: {inputs.attention_mask.shape} -> [batch_size, sequence_length]\n")
                    if "pixel_values" in inputs:
                        f.write(f"  inputs.pixel_values shape: {inputs.pixel_values.shape} -> [num_image_patches, feature_dim]\n")
                
                with torch.no_grad():
                    # Dynamically pass all tensors generated by the processor
                    forward_kwargs = {key: value for key, value in inputs.items()}
                    forward_kwargs["output_attentions"] = True
                    
                    outputs = model(**forward_kwargs)
                
                mean_attn = torch.mean(outputs.attentions[args.target_layer][0], dim=0)
                # Write attention shapes to log file
                with open(debug_log_path, "a") as f:
                    f.write(f"  Total attention layers: {len(outputs.attentions)} -> [number_of_transformer_blocks]\n")
                    f.write(f"  Raw Target Layer Attention shape: {outputs.attentions[args.target_layer].shape} -> [batch_size, num_heads, sequence_length, sequence_length]\n")
                    f.write(f"  mean_attn shape (averaged heads): {mean_attn.shape} -> [sequence_length, sequence_length]\n")
                
                input_ids_1d = inputs.input_ids[0]
                seq_len = len(input_ids_1d)
                
                # =========================================================================
                # NEW ROBUST MASKING: Array Divergence Mathematics
                # =========================================================================
                
                # 1. FIND EXACT IMAGE TOKENS
                # We tokenize the exact same prompt but omit the image object.
                # By comparing the arrays, we find exactly where the image was injected.
                msg_no_img = [
                    {"role": "user", "content": [{"type": "text", "text": final_text}]},
                    {"role": "assistant", "content": response_text}
                ]
                no_img_text = processor.apply_chat_template(msg_no_img, tokenize=False)
                ids_no_img = processor(text=no_img_text, return_tensors="pt").input_ids[0].to(device)
                
                div_img = 0
                while div_img < len(ids_no_img) and input_ids_1d[div_img] == ids_no_img[div_img]:
                    div_img += 1
                    
                num_image_tokens = len(input_ids_1d) - len(ids_no_img)
                is_image_token = torch.zeros(seq_len, dtype=torch.bool, device=device)
                if num_image_tokens > 0:
                    is_image_token[div_img : div_img + num_image_tokens] = True
                
                # 2. FIND EXACT ASSISTANT START
                msg_prompt = [
                    {"role": "user", "content": [{"type": "image"}, {"type": "text", "text": final_text}]}
                ]
                prompt_text = processor.apply_chat_template(msg_prompt, tokenize=False, add_generation_prompt=True)
                ids_prompt = processor(images=raw_image, text=prompt_text, return_tensors="pt").input_ids[0].to(device)
                assistant_start_idx = len(ids_prompt)
                
                # 3. FIND EXACT TEMPLATE START
                if user_prompt_template:
                    msg_no_temp = [
                        {"role": "user", "content": [{"type": "image"}, {"type": "text", "text": desc_text}]}
                    ]
                    no_temp_text = processor.apply_chat_template(msg_no_temp, tokenize=False, add_generation_prompt=True)
                    ids_no_temp = processor(images=raw_image, text=no_temp_text, return_tensors="pt").input_ids[0].to(device)
                    
                    div_temp = 0
                    while div_temp < len(ids_no_temp) and ids_prompt[div_temp] == ids_no_temp[div_temp]:
                        div_temp += 1
                    template_start_idx = div_temp
                else:
                    template_start_idx = assistant_start_idx

                # 4. BUILD THE PERFECT TEXT MASK
                text_start_idx = div_img + num_image_tokens
                is_text_token = torch.zeros(seq_len, dtype=torch.bool, device=device)
                is_text_token[text_start_idx:template_start_idx] = True

                N_image = is_image_token.sum().item()
                N_text = is_text_token.sum().item()

                # Write mask shapes and token counts to log file
                with open(debug_log_path, "a") as f:
                    f.write(f"  is_text_token mask shape: {is_text_token.shape} -> [sequence_length] (1D boolean array)\n")
                    f.write(f"  Valid Image Tokens (N_image): {N_image} | Valid Text Tokens (N_text): {N_text}\n")

                # Extract Timeseries Data
                timeseries_data = []
                token_counter = 1
                
                for gen_idx in range(assistant_start_idx + 1, seq_len):
                    gen_token_id = input_ids_1d[gen_idx]
                    gen_token_str = processor.tokenizer.decode([gen_token_id])
                    
                    attn_row = mean_attn[gen_idx - 1, :]
                    
                    A_image_raw = attn_row[is_image_token].sum().item()
                    A_text_raw = attn_row[is_text_token].sum().item()
                    
                    # Mean-Normalized Math
                    A_image_mean = A_image_raw / N_image if N_image > 0 else 0.0
                    A_text_mean = A_text_raw / N_text if N_text > 0 else 0.0
                    
                    IAR_norm = A_image_mean / (A_image_mean + A_text_mean) if (A_image_mean + A_text_mean) > 0 else 0.0
                    
                    timeseries_data.append({
                        "token_number_generated": token_counter,
                        "token_text": gen_token_str,
                        "IAR_normalized": round(IAR_norm, 4),    
                        "A_image_mean": round(A_image_mean, 6),  
                        "A_text_mean": round(A_text_mean, 6),    
                        "A_image_raw_sum": round(A_image_raw, 4), 
                        "A_text_raw_sum": round(A_text_raw, 4)    
                    })
                    token_counter += 1
                    
                # Save to CSV
                if timeseries_data:
                    csv_filename = f"{problem_id}_{variant}_layer{args.target_layer}.csv"
                    csv_path = os.path.join(out_dir, csv_filename)
                    pd.DataFrame(timeseries_data).to_csv(csv_path, index=False)
                
                # VRAM CLEANUP
                del outputs
                del inputs
                del mean_attn
                del stitched_text
                del messages
                
                gc.collect()
                torch.cuda.empty_cache()

    # Final cleanup when everything is done
    del model
    del processor
    torch.cuda.empty_cache()
    print("\n[SUCCESS] ALL SUBJECTS COMPLETED!")

if __name__ == "__main__":
    main()