import os
import json
import pandas as pd
import requests
import time
from tqdm import tqdm
from argparse import ArgumentParser

# ==========================================
# 1. USER CONFIGURATION
# ==========================================
# Paths & Directories
IMAGE_TEMP_DIR = "image_temp"
IMAGE_URLS_FILE = os.path.join(IMAGE_TEMP_DIR, "image_urls.json")
USER_PROMPT_PATH = "user_prompt.txt"
OPENROUTER_TEMP_DIR = "openrouter_temp"

# Experiment Scope
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
MAX_OUTPUT_TOKENS = 4096

os.makedirs(OPENROUTER_TEMP_DIR, exist_ok=True)

# ==========================================
# 2. ARGUMENT PARSING
# ==========================================
parser = ArgumentParser(description="Synchronous Stateful OpenRouter Inference Script")

# Workflow Flags
parser.add_argument("--process", action="store_true", help="Run the synchronous inference loop and save raw JSONs")
parser.add_argument("--extract", action="store_true", help="Extract text from saved JSONs and build Excel files")
parser.add_argument("--debug", action="store_true", help="Process only instance 00")
parser.add_argument("--model", type=str, required=True, help="Specific model to run (e.g., qwen/qwen-vl-plus:free)")
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

# OpenRouter API Config
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "https://github.com/falensiazmi/stem-vision", # Optional
    "X-OpenRouter-Title": "STEM-Vision Eval", # Optional
    "Content-Type": "application/json",
}

# ==========================================
# 3. DECOUPLED REQUEST FUNCTION
# ==========================================
def generate_openrouter_response(model_name, final_text, img_url):
    """
    Handles the synchronous OpenRouter API request.
    Returns the complete raw JSON response from the API.
    Guarantees success with a sentinel while loop.
    """
    payload = {
        "model": model_name,
        "temperature": TEMPERATURE,
        "max_tokens": MAX_OUTPUT_TOKENS,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": final_text},
                    {"type": "image_url", "image_url": {"url": img_url}}
                ]
            }
        ],
        'provider': {
            'order': ['alibaba'],
            'allow_fallbacks': False,
        },
    }

    # Sentinel loop to guarantee successful extraction
    while True:
        try:
            response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=120)
            
            if response.status_code != 200:
                # API level error (e.g., 502 Bad Gateway)
                print(f" [!] API Error {response.status_code}. Retrying in 2s...")
                time.sleep(2)
                continue
                
            res_json = response.json()
            
            if 'error' in res_json and res_json['error'] is not None:
                # OpenRouter explicit error response
                print(f" [!] OpenRouter Error: {res_json['error']}. Retrying in 2s...")
                time.sleep(2)
                continue
                
            if 'choices' in res_json and len(res_json['choices']) > 0:
                finish_reason = res_json['choices'][0].get('finish_reason')
                
                if finish_reason == "stop":
                    return res_json # RETURN ALL JSON ONLY ON SUCCESS
                else:
                    # e.g., "length" or "content_filter"
                    print(f" [!] Bad finish_reason ({finish_reason}). Retrying in 2s...")
                    time.sleep(2)
                    continue
            else:
                print(" [!] Malformed response (no choices). Retrying in 2s...")
                time.sleep(2)
                continue
                
        except Exception as e:
            # Network drops, timeouts, json decode errors
            print(f" [!] Request Exception: {str(e)}. Retrying in 2s...")
            time.sleep(2)
            continue

# ==========================================
# 4. WORKFLOW PIPELINE
# ==========================================
safe_model_name = args.model.replace("/", "_").replace(".", "_").replace(":", "_")
model_temp_dir = os.path.join(OPENROUTER_TEMP_DIR, safe_model_name)
status_file = os.path.join(OPENROUTER_TEMP_DIR, f"{safe_model_name}_status.json")

# ------------------------------------------
# STAGE: PROCESS
# ------------------------------------------
if args.process:
    print(f"\n{'='*60}\n[INFO] STARTING SYNCHRONOUS OPENROUTER INFERENCE\n{'='*60}")
    print(f"[INFO] Target Model: {args.model}")
    
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

    # 3. Setup Directories & Trackers
    os.makedirs(model_temp_dir, exist_ok=True)
    
    status_tracker = {}
    if os.path.exists(status_file):
        with open(status_file, 'r', encoding='utf-8') as f:
            status_tracker = json.load(f)

    error_logs = []

    # 4. Main Inference Loop
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
                
                print(f"\n -> Subject: {subject.upper()} | Instance: {idx_str} | Lang: {lang_key}")
                
                # Iterate through rows with a progress bar
                for row_idx, row in tqdm(df.iterrows(), total=len(df), desc="Requests", leave=False):
                    row_id = row['id']
                    custom_id = f"{subject}||{idx_str}||{row_id}||{lang_key}"
                    safe_custom_id = custom_id.replace("||", "_")
                    
                    # Changed to .json since we are storing the complete response
                    response_filepath = os.path.join(model_temp_dir, f"{safe_custom_id}.json")
                    
                    img_rel_path = row["image"].replace("\\", "/")
                    full_local_path = f"{idx_str}/{subject}/{img_rel_path}" # Excludes 'sample/' prefix
                    img_url = image_url_map.get(full_local_path)
                    
                    if not img_url:
                        error_logs.append(f"[{args.model}] {custom_id}: [ERROR: IMAGE URL NOT FOUND]")
                        continue

                    # Stateful Check: Skip API call if already completed successfully
                    if status_tracker.get(custom_id) == "COMPLETED" and os.path.exists(response_filepath):
                        continue

                    base_desc = str(row[desc_col])
                    final_text = f"{base_desc}\n\n{user_prompt_template}" if user_prompt_template else base_desc

                    # Delegate to the decoupled API function
                    try:
                        res_json = generate_openrouter_response(
                            model_name=args.model,
                            final_text=final_text,
                            img_url=img_url
                        )
                        
                        # Save entire JSON response to file
                        with open(response_filepath, 'w', encoding='utf-8') as f:
                            json.dump(res_json, f, indent=4, ensure_ascii=False)
                            
                        # Update Checkpoint JSON
                        status_tracker[custom_id] = "COMPLETED"
                        with open(status_file, 'w', encoding='utf-8') as f:
                            json.dump(status_tracker, f, indent=4)
                            
                    except Exception as e:
                        error_msg = f"[REQUEST EXCEPTION] {str(e)}"
                        error_logs.append(f"[{args.model}] {custom_id}: {error_msg}")

    # Write error recap if any occurred
    if error_logs:
        log_path = f"openrouter_{safe_model_name}_failures.log"
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write(f"=== OPENROUTER FAILURES LOG ({args.model}) ===\n")
            for log_msg in error_logs:
                f.write(log_msg + "\n")
        print(f"\n[INFO] Failure recap saved to {log_path}")

# ------------------------------------------
# STAGE: EXTRACT
# ------------------------------------------
if args.extract:
    print(f"\n{'='*60}\n[INFO] EXTRACTING SAVED JSONS TO EXCEL\n{'='*60}")
    print(f"[INFO] Target Model: {args.model}")
    
    if not os.path.exists(model_temp_dir):
        print(f"[!] Error: No saved responses found in {model_temp_dir}. Run --process first.")
        exit()

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
                
                for row_idx, row in df.iterrows():
                    row_id = row['id']
                    custom_id = f"{subject}||{idx_str}||{row_id}||{lang_key}"
                    safe_custom_id = custom_id.replace("||", "_")
                    response_filepath = os.path.join(model_temp_dir, f"{safe_custom_id}.json")
                    
                    if os.path.exists(response_filepath):
                        try:
                            with open(response_filepath, 'r', encoding='utf-8') as f:
                                res_json = json.load(f)
                                
                            # Safe extraction
                            if 'error' in res_json:
                                answer = f"[API ERROR] {res_json['error']}"
                            else:
                                answer = res_json['choices'][0]['message']['content']
                                
                            df.at[row_idx, lang_key] = answer
                        except Exception as e:
                            df.at[row_idx, lang_key] = f"[EXTRACTION ERROR] {str(e)}"
                    else:
                        df.at[row_idx, lang_key] = "[NO RESPONSE SAVED]"

            # Export reconstructed DataFrame to Excel
            output_path = os.path.join('result', 'raw', subject, idx_str)
            os.makedirs(output_path, exist_ok=True)
            full_output_path = os.path.join(output_path, f"{safe_model_name}.xlsx")
            
            df.to_excel(full_output_path, index=False, engine="openpyxl")
            print(f" [SUCCESS] Extracted and Saved -> {full_output_path}")

if not args.process and not args.extract:
    print("\n[INFO] No action specified. Use --process or --extract.")

print("\n[INFO] Execution Finished.")