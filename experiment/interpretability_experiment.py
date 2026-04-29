import os
import glob
import argparse
import pandas as pd
import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM

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
    out_dir = os.path.join("result", "process", "attention_timeseries", args.model_name.replace("/", "_"), args.subject, args.instance)
    os.makedirs(out_dir, exist_ok=True)
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[INFO] Using device: {device} | Target Layer: {args.target_layer}")

    # 2. Load Model & Processor
    print(f"[INFO] Loading model: {args.model_name}")
    processor = AutoProcessor.from_pretrained(args.model_name)
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name, 
        torch_dtype=torch.bfloat16, 
        device_map="auto"
    )
    
    try:
        image_pad_id = processor.tokenizer.convert_tokens_to_ids("<|image_pad|>")
    except:
        image_pad_id = None
        print("[WARNING] Could not find <|image_pad|> token ID.")

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
    for _, row in df.iterrows():
        problem_id = row.get("id", "unknown")
        print(f"\n[INFO] Processing Problem: {problem_id}")
        
        image_path = os.path.join("experiment", "sample", args.instance, args.subject, str(row["image"]))
        try:
            raw_image = Image.open(image_path).convert("RGB")
        except Exception as e:
            print(f"[ERROR] Could not load image {image_path}: {e}")
            continue

        for desc_col in desc_cols:
            variant = desc_col.replace("description_", "") if desc_col != "description" else "en"
            response_col = desc_col.replace("description", "response")
            
            if response_col not in row or pd.isna(row[response_col]):
                continue
                
            desc_text = str(row[desc_col])
            response_text = str(row[response_col])
            
            # Stitching
            messages = [
                {"role": "user", "content": [{"type": "image"}, {"type": "text", "text": desc_text}]},
                {"role": "assistant", "content": response_text}
            ]
            
            stitched_text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
            
            inputs = processor(
                images=raw_image, 
                text=stitched_text, 
                return_tensors="pt"
            ).to(device)
            
            # Forward Pass (ONE pass gets us all tokens' attention!)
            with torch.no_grad():
                forward_kwargs = {"input_ids": inputs.input_ids, "attention_mask": inputs.attention_mask, "output_attentions": True}
                if "pixel_values" in inputs: forward_kwargs["pixel_values"] = inputs.pixel_values
                if "image_grid_thw" in inputs: forward_kwargs["image_grid_thw"] = inputs.image_grid_thw
                
                outputs = model(**forward_kwargs)
            
            # Extract Attention for the specified layer
            # Shape: [Seq_Len, Seq_Len]
            mean_attn = torch.mean(outputs.attentions[args.target_layer][0], dim=0)
            input_ids_1d = inputs.input_ids[0]
            seq_len = len(input_ids_1d)
            
            # Define Masks
            is_image_token = (input_ids_1d == image_pad_id)
            
            # Find where assistant starts generating
            assistant_token_id = processor.tokenizer.convert_tokens_to_ids("assistant")
            try:
                # Find the last occurrence of the "assistant" token
                assistant_start_idx = (input_ids_1d == assistant_token_id).nonzero(as_tuple=True)[0][-1].item()
            except:
                print(f"  [WARNING] Could not find assistant start for {variant}. Skipping.")
                continue

            is_prompt_token = torch.arange(seq_len, device=device) <= assistant_start_idx
            is_text_token = is_prompt_token & ~is_image_token

            # 5. Extract Timeseries Data
            timeseries_data = []
            token_counter = 1
            
            # We loop over the generated tokens. 
            # If a token is at index `gen_idx`, the attention used to generate it is at row `gen_idx - 1`
            for gen_idx in range(assistant_start_idx + 1, seq_len):
                gen_token_id = input_ids_1d[gen_idx]
                gen_token_str = processor.tokenizer.decode([gen_token_id])
                
                attn_row = mean_attn[gen_idx - 1, :]
                
                A_image = attn_row[is_image_token].sum().item()
                A_text = attn_row[is_text_token].sum().item()
                IAR = A_image / (A_image + A_text) if (A_image + A_text) > 0 else 0.0
                
                timeseries_data.append({
                    "token_number_generated": token_counter,
                    "token_text": gen_token_str, # Highly recommended so you can read the CSV!
                    "image_attention_ratio": round(IAR, 4),
                    "A_image_raw": round(A_image, 4),
                    "A_text_raw": round(A_text, 4)
                })
                token_counter += 1
                
            # 6. Save to CSV
            if timeseries_data:
                csv_filename = f"{problem_id}_{variant}_layer{args.target_layer}.csv"
                csv_path = os.path.join(out_dir, csv_filename)
                pd.DataFrame(timeseries_data).to_csv(csv_path, index=False)
                print(f"  -> Saved timeseries: {csv_filename}")

    # Cleanup
    del model
    del processor
    torch.cuda.empty_cache()

if __name__ == "__main__":
    main()