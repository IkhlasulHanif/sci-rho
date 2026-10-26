import os
import json
import pandas as pd
import requests
import time
from tqdm import tqdm
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor, as_completed

# ==========================================
# 1. USER CONFIGURATION
# ==========================================
# Paths & Directories
IMAGE_TEMP_DIR = "image_temp"
IMAGE_URLS_FILE = os.path.join(IMAGE_TEMP_DIR, "image_urls.json") # Default
USER_PROMPT_PATH = "user_prompt.txt"
OPENROUTER_TEMP_DIR = "openrouter_temp"

# Experiment Scope (Default)
SUBJECTS = [
    "mathematics", 
    "physics", 
    "chemistry", 
    "biology", 
    "compsci"
]
DEFAULT_NUM_INSTANCES = 10

os.makedirs(OPENROUTER_TEMP_DIR, exist_ok=True)

# MAPPING PROVIDER
provider_mapper = {
    'qwen/qwen3.5-122b-a10b': 'alibaba',
    'qwen/qwen3.5-27b': 'alibaba',
    'meta-llama/llama-4-scout': 'google-vertex',
    'google/gemma-3-27b-it': 'phala'
}

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
BASE_SAMPLE_DIR = "sample"
PREFIX = ""

# Sampling Parameters
if args.model in ['qwen/qwen3.5-122b-a10b', 'qwen/qwen3.5-27b']:
    TEMPERATURE = 1.0
    MAX_OUTPUT_TOKENS = 8192
else:
    TEMPERATURE = 0.0
    MAX_OUTPUT_TOKENS = 4096

PROVIDER = provider_mapper.get(args.model, '')

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
    "HTTP-Referer": "https://github.com/falensiazmi/sci-rho", # Optional
    "X-OpenRouter-Title": "Sci-Rho Eval", # Optional
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
        "max_completion_tokens": MAX_OUTPUT_TOKENS,
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
            'order': [PROVIDER],
            'allow_fallbacks': False,
        },
        "reasoning":{
            "enabled" : False
        },
    }

    # Sentinel loop to guarantee successful extraction
    attempt = 0
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
                
                # Added 'end_turn' and 'eos_token' to handle different provider standards
                if finish_reason in ["stop", "end_turn", "eos_token", "length"]:
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
            attempt += 1
            delay = min(60, 2 ** attempt) # Waits 2s, 4s, 8s, 16s... capped at 60s
            print(f" [!] Request Exception: {str(e)}. Retrying in {delay}s...")
            time.sleep(delay)
            continue

# ==========================================
# 4. WORKFLOW PIPELINE
# ==========================================
job_key = f"{PREFIX}{args.model}"
safe_model_name = job_key.replace("/", "_").replace(".", "_").replace(":", "_")
model_temp_dir = os.path.join(OPENROUTER_TEMP_DIR, safe_model_name)
status_file = os.path.join(OPENROUTER_TEMP_DIR, f"{safe_model_name}_status.json")
responses_file = os.path.join(model_temp_dir, f"{safe_model_name}_responses.jsonl")

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
    pending_responses = []
    new_data_count = 0
    tasks = []

    # 4. Gather All Tasks First
    print("\n[*] Gathering tasks...")
    for subject in SUBJECTS:
        for index in range(NUM_OF_INSTANCES):
            idx_str = f"0{index}"
            dataset_path = os.path.join(BASE_SAMPLE_DIR, idx_str, subject)
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
                
                for row_idx, row in df.iterrows():
                    row_id = row['id']
                    custom_id = f"{subject}||{idx_str}||{row_id}||{lang_key}"
                    
                    img_rel_path = row["image"].replace("\\", "/")
                    full_local_path = f"{idx_str}/{subject}/{img_rel_path}" # Excludes base sample dir prefix
                    img_url = image_url_map.get(full_local_path)
                    
                    if not img_url:
                        error_logs.append(f"[{args.model}] {custom_id}: [ERROR: IMAGE URL NOT FOUND]")
                        continue

                    # Stateful Check: Skip if already completed
                    if status_tracker.get(custom_id) == "COMPLETED":
                        continue

                    base_desc = str(row[desc_col])
                    final_text = f"{base_desc}\n\n{user_prompt_template}" if user_prompt_template else base_desc

                    tasks.append({
                        "custom_id": custom_id,
                        "final_text": final_text,
                        "img_url": img_url
                    })

    # 5. Execute Tasks in Parallel
    print(f"[*] Total pending requests: {len(tasks)}")
    MAX_WORKERS = 10 # Adjust based on OpenRouter's rate limits

    if tasks:
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            # Map futures to their original task data
            future_to_task = {
                executor.submit(generate_openrouter_response, args.model, t["final_text"], t["img_url"]): t
                for t in tasks
            }
            
            # as_completed yields on the main thread, avoiding race conditions for file I/O
            for future in tqdm(as_completed(future_to_task), total=len(tasks), desc="Processing Requests"):
                task = future_to_task[future]
                custom_id = task["custom_id"]
                
                try:
                    res_json = future.result()
                    
                    # Add response to batch list 
                    pending_responses.append({"custom_id": custom_id, "response": res_json})
                    status_tracker[custom_id] = "COMPLETED"
                    new_data_count += 1
                    
                    # Batch flush to JSONL every 10 rows to prevent overhead
                    if new_data_count >= 10:
                        with open(responses_file, 'a', encoding='utf-8') as f:
                            for record in pending_responses:
                                f.write(json.dumps(record, ensure_ascii=False) + "\n")
                        
                        with open(status_file, 'w', encoding='utf-8') as f:
                            json.dump(status_tracker, f, indent=4)
                            
                        pending_responses = []
                        new_data_count = 0
                        
                except Exception as e:
                    error_msg = f"[THREAD EXCEPTION] {str(e)}"
                    error_logs.append(f"[{args.model}] {custom_id}: {error_msg}")

    # Flush remaining responses after all loops are finished
    if pending_responses:
        with open(responses_file, 'a', encoding='utf-8') as f:
            for record in pending_responses:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
        
        with open(status_file, 'w', encoding='utf-8') as f:
            json.dump(status_tracker, f, indent=4)

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

    # Load all saved JSONL responses into memory for fast lookup
    responses_dict = {}
    if os.path.exists(responses_file):
        with open(responses_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    record = json.loads(line)
                    responses_dict[record['custom_id']] = record['response']

    for subject in SUBJECTS:
        for index in range(NUM_OF_INSTANCES):
            idx_str = f"0{index}"
            dataset_path = os.path.join(BASE_SAMPLE_DIR, idx_str, subject)
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
                    
                    if custom_id in responses_dict:
                        try:
                            res_json = responses_dict[custom_id]
                                
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
            # Use original model name for excel file so it matches downstream scripts
            excel_name = args.model.replace("/", "_").replace(".", "_").replace(":", "_")
            full_output_path = os.path.join(output_path, f"{excel_name}.xlsx")
            
            df.to_excel(full_output_path, index=False, engine="openpyxl")
            print(f" [SUCCESS] Extracted and Saved -> {full_output_path}")

if not args.process and not args.extract:
    print("\n[INFO] No action specified. Use --process or --extract.")

print("\n[INFO] Execution Finished.")