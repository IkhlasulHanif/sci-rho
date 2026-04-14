import os
import json
import pandas as pd
import requests
from tqdm import tqdm
from argparse import ArgumentParser

# ==========================================
# 1. USER CONFIGURATION
# ==========================================
# Paths & Directories
IMAGE_TEMP_DIR = "image_temp"
IMAGE_URLS_FILE = os.path.join(IMAGE_TEMP_DIR, "image_urls.json")
USER_PROMPT_PATH = "user_prompt.txt"

# Experiment Scope
MODELS = [
    "qwen/qwen-vl-plus:free", # Change to "qwen/qwen3.5-122b-a10b" or your specific Qwen model
]
SUBJECTS = [
    "mathematics", 
    "physics", 
    "chemistry", 
    "biology", 
    "compsci"
]
DEFAULT_NUM_INSTANCES = 5

# Sampling Parameters
TEMPERATURE = 0.0
MAX_TOKENS = 4096

# ==========================================
# 2. ARGUMENT PARSING
# ==========================================
parser = ArgumentParser(description="Synchronous OpenRouter Inference Script")

# Workflow Flags
parser.add_argument("--process", action="store_true", help="Run the synchronous inference loop")
parser.add_argument("--debug", action="store_true", help="Process only instance 00")
args = parser.parse_args()

NUM_OF_INSTANCES = 1 if args.debug else DEFAULT_NUM_INSTANCES

# Load API Key
API_KEY_PATH = os.path.join('secrets', 'openrouter_api_key.txt')
try:
    with open(API_KEY_PATH, 'r') as f:
        API_KEY = f.readline().strip()
except FileNotFoundError:
    print(f"[!] Error: OpenRouter API key not found at {API_KEY_PATH}")
    exit(1)

# ==========================================
# 3. WORKFLOW PIPELINE
# ==========================================

if args.process:
    print(f"\n{'='*60}\n[INFO] STARTING SYNCHRONOUS OPENROUTER INFERENCE\n{'='*60}")
    
    # 1. Load Image Map
    if not os.path.exists(IMAGE_URLS_FILE):
        raise FileNotFoundError(f"Image URLs map not found at {IMAGE_URLS_FILE}.")
    with open(IMAGE_URLS_FILE, 'r', encoding='utf-8') as f:
        image_url_map = json.load(f)

    # 2. Load User Prompt
    user_prompt_template = ""
    if os.path.exists(USER_PROMPT_PATH):
        with open(USER_PROMPT_PATH, "r", encoding="utf-8") as f:
            user_prompt_template = f.read().strip()
        print(f"[INFO] Loaded additional prompt template from {USER_PROMPT_PATH}")

    # 3. OpenRouter API Config
    OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/your-repo", # Optional
        "X-OpenRouter-Title": "STEM-Vision Eval" # Optional
    }

    error_logs = []

    # 4. Main Inference Loop
    for model_name in MODELS:
        print(f"\n[INFO] Processing Model: {model_name}")
        safe_model_name = model_name.replace("/", "_").replace(".", "_").replace(":", "_")
        
        for subject in SUBJECTS:
            for index in range(NUM_OF_INSTANCES):
                idx_str = f"0{index}"
                dataset_path = os.path.join("sample", idx_str, subject)
                json_path = os.path.join(dataset_path, 'dataset.json')
                
                if not os.path.exists(json_path): continue
                
                with open(json_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                
                df = pd.DataFrame.from_dict(data, orient="index")
                if len(df) == 0: continue
                df.insert(0, "id", range(1, len(df) + 1))
                
                desc_columns = [col for col in df.columns if col.startswith("description")]
                
                for desc_col in desc_columns:
                    lang_key = desc_col.replace("description", "response")
                    df[lang_key] = "" # Initialize column
                    
                    print(f" -> Subject: {subject.upper()} | Instance: {idx_str} | Lang: {lang_key}")
                    
                    # Iterate through rows with a progress bar
                    for row_idx, row in tqdm(df.iterrows(), total=len(df), desc="Requests", leave=False):
                        img_rel_path = row["image"].replace("\\", "/")
                        full_local_path = f"sample/{idx_str}/{subject}/{img_rel_path}"
                        img_url = image_url_map.get(full_local_path)
                        
                        if not img_url:
                            df.at[row_idx, lang_key] = "[ERROR: IMAGE URL NOT FOUND]"
                            continue

                        base_desc = str(row[desc_col])
                        final_text = f"{base_desc}\n\n{user_prompt_template}" if user_prompt_template else base_desc

                        # Prepare Payload
                        payload = {
                            "model": model_name,
                            "temperature": TEMPERATURE,
                            "max_tokens": MAX_TOKENS,
                            "messages": [
                                {
                                    "role": "user",
                                    "content": [
                                        {"type": "text", "text": final_text},
                                        {"type": "image_url", "image_url": {"url": img_url}}
                                    ]
                                }
                            ]
                        }

                        # API Call with Error Handling
                        try:
                            response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=120)
                            
                            if response.status_code == 200:
                                res_json = response.json()
                                answer = res_json['choices'][0]['message']['content']
                                df.at[row_idx, lang_key] = answer
                            else:
                                error_msg = f"[API ERROR {response.status_code}] {response.text}"
                                df.at[row_idx, lang_key] = error_msg
                                error_logs.append(f"[{model_name}] {subject}-{idx_str}-Row{row['id']}: {error_msg}")
                                
                        except Exception as e:
                            error_msg = f"[REQUEST EXCEPTION] {str(e)}"
                            df.at[row_idx, lang_key] = error_msg
                            error_logs.append(f"[{model_name}] {subject}-{idx_str}-Row{row['id']}: {error_msg}")

                # Save immediately after finishing the instance to prevent data loss
                output_path = os.path.join('result', 'raw', subject, idx_str)
                os.makedirs(output_path, exist_ok=True)
                full_output_path = os.path.join(output_path, f"{safe_model_name}.xlsx")
                
                df.to_excel(full_output_path, index=False, engine="openpyxl")
                print(f" [SUCCESS] Saved -> {full_output_path}")

    # Write error recap if any occurred
    if error_logs:
        log_path = "openrouter_failures.log"
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write("=== OPENROUTER FAILURES LOG ===\n")
            for log_msg in error_logs:
                f.write(log_msg + "\n")
        print(f"\n[INFO] Failure recap saved to {log_path}")

print("\n[INFO] Execution Finished.")