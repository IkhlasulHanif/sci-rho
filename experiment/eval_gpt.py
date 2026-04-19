import os
import json
import pandas as pd
from argparse import ArgumentParser
from openai import OpenAI

# ==========================================
# 1. USER CONFIGURATION
# ==========================================
# Paths & Directories
GPT_TEMP_DIR = "gpt_temp"
IMAGE_TEMP_DIR = "image_temp"
IMAGE_URLS_FILE = os.path.join(IMAGE_TEMP_DIR, "image_urls.json")
BATCH_JOBS_FILE = os.path.join(GPT_TEMP_DIR, "batch_jobs.json")
USER_PROMPT_PATH = "user_prompt.txt"

# Experiment Scope
MODELS = [
    "gpt-5",
    # "gpt-5-nano-2025-08-07" # for testing
]
SUBJECTS = [
    "mathematics", 
    "physics", 
    "chemistry", 
    "biology", 
    "compsci"
]
DEFAULT_NUM_INSTANCES = 10
REASONING_EFFORT = "none"

# Sampling Parameters
TEMPERATURE = 1.0
MAX_NEW_TOKENS = 8192

os.makedirs(GPT_TEMP_DIR, exist_ok=True)

# ==========================================
# 2. ARGUMENT PARSING
# ==========================================
parser = ArgumentParser(description="Stateful OpenAI Batch Inference Script")

# Workflow Flags
parser.add_argument("--prepare", action="store_true", help="Generate local .jsonl requests for OpenAI")
parser.add_argument("--debug", action="store_true", help="Process only instance 00 (Use with --prepare)")
parser.add_argument("--send", action="store_true", help="Send prepared .jsonl requests to OpenAI Batch API")
parser.add_argument("--check", action="store_true", help="Check status of active batches")
parser.add_argument("--retrieve", action="store_true", help="Download results and reconstruct Excel files")
args = parser.parse_args()

NUM_OF_INSTANCES = 1 if args.debug else DEFAULT_NUM_INSTANCES

# put API key to `secrets/openai_api_key.txt`
# otherwise, use environment variables
API_KEY_PATH = os.path.join('secrets', 'openai_api_key.txt')
try:
    with open(API_KEY_PATH, 'r') as f:
        API_KEY = f.readline().strip()
    client = OpenAI(api_key=API_KEY)
except:
    client = OpenAI()

# ==========================================
# 3. WORKFLOW PIPELINE
# ==========================================

if args.prepare:
    print(f"\n{'='*60}\n[INFO] STAGE 1: PREPARING BATCH REQUESTS\n{'='*60}")
    
    if not os.path.exists(IMAGE_URLS_FILE):
        raise FileNotFoundError(f"Image URLs map not found at {IMAGE_URLS_FILE}. Run your crawler first.")
    with open(IMAGE_URLS_FILE, 'r') as f:
        image_url_map = json.load(f)

    # Load User Prompt
    user_prompt_template = ""
    if os.path.exists(USER_PROMPT_PATH):
        with open(USER_PROMPT_PATH, "r", encoding="utf-8") as f:
            user_prompt_template = f.read().strip()
        print(f"[INFO] Loaded additional prompt template from {USER_PROMPT_PATH}")

    for model_name in MODELS:
        safe_model_name = model_name.replace("/", "_").replace(".", "_")
        jsonl_filename = os.path.join(GPT_TEMP_DIR, f"req_{safe_model_name}.jsonl")
        
        # Safety Check: Do not overwrite existing preparation files
        if os.path.exists(jsonl_filename):
            print(f"[!] Safety Check: '{jsonl_filename}' already exists. Skipping preparation for {model_name}.")
            continue

        print(f"\n[INFO] Preparing Requests for Model: {model_name}")
        batch_requests = []
        
        for subject in SUBJECTS:
            for index in range(NUM_OF_INSTANCES):
                # Physical files are still inside 'sample/'
                dataset_path = os.path.join("sample", f"0{index}", subject)
                json_path = os.path.join(dataset_path, 'dataset.json')
                
                if not os.path.exists(json_path): continue
                with open(json_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                
                df = pd.DataFrame.from_dict(data, orient="index")
                if len(df) == 0: continue
                df.insert(0, "id", range(1, len(df) + 1))
                
                desc_columns = [col for col in df.columns if col.startswith("description")]
                
                for desc_col in desc_columns:
                    lang_suffix = desc_col.replace("description", "response")
                    
                    for _, row in df.iterrows():
                        # Create unique Custom ID -> "physics||00||12||response_indonesian"
                        custom_id = f"{subject}||0{index}||{row['id']}||{lang_suffix}"
                        
                        # Reconstruct the precise local path to match the image_urls.json key
                        img_rel_path = row["image"].replace("\\", "/")
                        # The JSON key dropped the 'sample/' prefix
                        full_local_path = f"0{index}/{subject}/{img_rel_path}"
                        img_url = image_url_map.get(full_local_path)
                        
                        if not img_url:
                            print(f"[!] Warning: No URL mapped for {full_local_path}. Skipping.")
                            continue

                        # Construct Final Text
                        base_desc = str(row[desc_col])
                        if user_prompt_template:
                            final_text = f"{base_desc}\n\n{user_prompt_template}"
                        else:
                            print("[!] ERROR: PROMPT TEMPLATE NOT FOUND")
                            exit()

                        request = {
                            "custom_id": custom_id,
                            "method": "POST",
                            "url": "/v1/chat/completions",
                            "body": {
                                "model": model_name,
                                "temperature": TEMPERATURE,
                                "max_completion_tokens": MAX_NEW_TOKENS,
                                "reasoning_effort": REASONING_EFFORT,
                                "messages": [
                                    {"role": "user", "content": [
                                        {"type": "text", "text": final_text},
                                        {"type": "image_url", "image_url": {"url": img_url}}
                                    ]}
                                ]
                            }
                        }
                        batch_requests.append(request)
        
        with open(jsonl_filename, 'w', encoding='utf-8') as f:
            for req in batch_requests:
                # ensure_ascii=False handles Hindi, Arabic, Chinese, Kazakh properly
                f.write(json.dumps(req, ensure_ascii=False) + "\n")
        print(f"[INFO] Prepared {len(batch_requests)} requests -> {jsonl_filename}")


if args.send:
    print(f"\n{'='*60}\n[INFO] STAGE 2: SENDING BATCHES TO OPENAI\n{'='*60}")
    
    batch_jobs = {}
    if os.path.exists(BATCH_JOBS_FILE):
        with open(BATCH_JOBS_FILE, 'r') as f:
            batch_jobs = json.load(f)

    for model_name in MODELS:
        safe_model_name = model_name.replace("/", "_").replace(".", "_")
        jsonl_filename = os.path.join(GPT_TEMP_DIR, f"req_{safe_model_name}.jsonl")
        
        if not os.path.exists(jsonl_filename):
            print(f"[SKIP] No jsonl file found for {model_name}.")
            continue
            
        print(f"[INFO] Uploading file to OpenAI for {model_name}...")
        with open(jsonl_filename, "rb") as file_obj:
            batch_file = client.files.create(file=file_obj, purpose="batch")
        
        print(f"[INFO] Triggering Batch API for {model_name}...")
        batch_job = client.batches.create(
            input_file_id=batch_file.id,
            endpoint="/v1/chat/completions",
            completion_window="24h"
        )
        
        batch_jobs[model_name] = {
            "batch_id": batch_job.id,
            "input_file_id": batch_file.id,
            "status": batch_job.status
        }
        print(f"[SUCCESS] Submitted! Batch ID: {batch_job.id}")

    with open(BATCH_JOBS_FILE, 'w') as f:
        json.dump(batch_jobs, f, indent=4)


if args.check:
    print(f"\n{'='*60}\n[INFO] STAGE 3: CHECKING BATCH STATUS\n{'='*60}")
    
    if not os.path.exists(BATCH_JOBS_FILE):
        print("[INFO] No active batches found in tracking file.")
        exit()
        
    with open(BATCH_JOBS_FILE, 'r') as f:
        batch_jobs = json.load(f)
        
    all_ready = True
    for model_name, job_info in batch_jobs.items():
        job_status = client.batches.retrieve(job_info["batch_id"])
        batch_jobs[model_name]["status"] = job_status.status
        
        status_str = job_status.status.upper()
        print(f"Model: {model_name.ljust(30)} | Status: {status_str}")
        
        if status_str != "COMPLETED":
            all_ready = False
            
    with open(BATCH_JOBS_FILE, 'w') as f:
        json.dump(batch_jobs, f, indent=4)
        
    print("\n------------------------------------------------------------")
    if all_ready:
        print("[READY] All batches are completed! You can now run with --retrieve")
    else:
        print("[WAIT] Batches are still processing. Check again later.")


if args.retrieve:
    print(f"\n{'='*60}\n[INFO] STAGE 4: RETRIEVING & SAVING RESULTS\n{'='*60}")
    
    if not os.path.exists(BATCH_JOBS_FILE):
        print("[!] No batches tracking file found to retrieve.")
        exit()
        
    with open(BATCH_JOBS_FILE, 'r') as f:
        batch_jobs = json.load(f)

    for model_name, job_info in batch_jobs.items():
        safe_model_name = model_name.replace("/", "_").replace(".", "_")
        request_logs = []  # Detailed log for every individual request
        
        if job_info["status"] != "completed":
            log_msg = f"[SKIP] {model_name}: Status is '{job_info['status']}' (Needs to be 'completed')"
            print(log_msg)
            continue
            
        print(f"\n[INFO] Retrieving results for {model_name}...")
        job_status = client.batches.retrieve(job_info["batch_id"])
        
        if not job_status.output_file_id:
            log_msg = f"[!] Warning: No output file generated for {model_name}"
            print(log_msg)
            request_logs.append(log_msg)
            
            # If batch failed, it might have an error file instead
            if getattr(job_status, 'error_file_id', None):
                error_content = client.files.content(job_status.error_file_id).text
                request_logs.append(f"[{model_name}] Error File Content:\n{error_content}")
            
            # Save logs before continuing to the next model (Safety check removed per previous request)
            log_path = os.path.join(GPT_TEMP_DIR, f"{safe_model_name}_requests.log")
            with open(log_path, 'w', encoding='utf-8') as f:
                f.write(f"=== REQUEST LOGS FOR {model_name} ===\n")
                for msg in request_logs: f.write(msg + "\n")
            print(f"\n[INFO] Detailed request logs saved to {log_path}")
            continue
            
        # Download the JSONL output from OpenAI
        result_content = client.files.content(job_status.output_file_id).text
        
        # Structure: mapped_results[subject][instance_str][row_id_str][lang_suffix] = response_text
        mapped_results = {}
        error_count = 0
        
        for line in result_content.strip().split('\n'):
            if not line: continue
            res = json.loads(line)
            
            # Handle potential missing custom_id safely
            custom_id = res.get('custom_id', 'UNKNOWN||UNKNOWN||UNKNOWN||UNKNOWN')
            subj, idx_str, row_id, lang = custom_id.split("||")
            
            try:
                # Check for top-level API errors inside the response payload
                if 'error' in res and res['error'] is not None:
                    answer = f"[API ERROR] {res['error']}"
                    error_count += 1
                    request_logs.append(f"[{model_name}] FAILED  | ID: {custom_id} | API Error: {res['error']}")
                else:
                    answer = res['response']['body']['choices'][0]['message']['content']
                    request_logs.append(f"[{model_name}] SUCCESS | ID: {custom_id}")
            except Exception as e:
                answer = "[ERROR GENERATING RESPONSE]"
                error_count += 1
                error_details = res.get('error', str(e))
                request_logs.append(f"[{model_name}] FAILED  | ID: {custom_id} | Exception: {error_details}")
                
            if subj not in mapped_results: mapped_results[subj] = {}
            if idx_str not in mapped_results[subj]: mapped_results[subj][idx_str] = {}
            if row_id not in mapped_results[subj][idx_str]: mapped_results[subj][idx_str][row_id] = {}
            
            mapped_results[subj][idx_str][row_id][lang] = answer

        if error_count > 0:
            print(f"[!] Warning: {error_count} responses failed to generate correctly.")

        # Reconstruct DataFrames & Export to Excel
        for subject in SUBJECTS:
            for index in range(NUM_OF_INSTANCES):
                idx_str = f"0{index}"
                
                # Skip if no data was returned for this subject/instance combo
                if subject not in mapped_results or idx_str not in mapped_results[subject]:
                    continue
                    
                # Physical files are still inside 'sample/'
                dataset_path = os.path.join("sample", idx_str, subject)
                json_path = os.path.join(dataset_path, 'dataset.json')
                
                if not os.path.exists(json_path): continue
                with open(json_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    
                df = pd.DataFrame.from_dict(data, orient="index")
                df.insert(0, "id", range(1, len(df) + 1))
                
                desc_columns = [col for col in df.columns if col.startswith("description")]
                for desc_col in desc_columns:
                    # e.g., 'description_indonesian' -> 'response_indonesian'
                    lang_key = desc_col.replace("description", "response") 
                    
                    # Apply mapped answers using the row 'id'
                    df[lang_key] = df["id"].apply(
                        lambda r_id: mapped_results[subject][idx_str].get(str(r_id), {}).get(lang_key, "")
                    )

                output_path = os.path.join('result', 'raw', subject, idx_str)
                os.makedirs(output_path, exist_ok=True)
                full_output_path = os.path.join(output_path, f"{safe_model_name}.xlsx")
                
                # Safety Check: Do not overwrite existing Excel results
                if os.path.exists(full_output_path):
                    print(f"[!] Safety Check: '{full_output_path}' already exists. Skipping Excel save.")
                else:
                    df.to_excel(full_output_path, index=False, engine="openpyxl")
                    print(f"[SUCCESS] Saved Excel -> {full_output_path}")

        # Write detailed request logs for this model (Always overwrites per previous request)
        if request_logs:
            log_path = os.path.join(GPT_TEMP_DIR, f"{safe_model_name}_requests.log")
            with open(log_path, 'w', encoding='utf-8') as f:
                f.write(f"=== REQUEST LOGS FOR {model_name} ===\n")
                for log_msg in request_logs:
                    f.write(log_msg + "\n")
            print(f"\n[INFO] Detailed request logs saved to {log_path}")

print("\n[INFO] Execution Finished.")