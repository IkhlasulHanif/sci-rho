import os
import json
import pandas as pd
from argparse import ArgumentParser
import anthropic

# ==========================================
# 1. USER CONFIGURATION
# ==========================================
# Paths & Directories
CLAUDE_TEMP_DIR = "claude_temp"
IMAGE_TEMP_DIR = "image_temp"
IMAGE_URLS_FILE = os.path.join(IMAGE_TEMP_DIR, "image_urls.json")
BATCH_JOBS_FILE = os.path.join(CLAUDE_TEMP_DIR, "batch_jobs.json")
USER_PROMPT_PATH = "user_prompt.txt"

# Experiment Scope
MODELS = [
    "claude-sonnet-4-6", 
    "claude-haiku-4-5-20251001"
]
SUBJECTS = [
    "mathematics", 
    "physics", 
    "chemistry", 
    "biology", 
    "compsci"
]
DEFAULT_NUM_INSTANCES = 5

# Sampling & Thinking Parameters
TEMPERATURE = 0.0
MAX_TOKENS = 8192
ENABLE_THINKING = False  # Toggle to True if using models that support Extended Thinking (requires temp=1.0)

os.makedirs(CLAUDE_TEMP_DIR, exist_ok=True)

# ==========================================
# 2. ARGUMENT PARSING
# ==========================================
parser = ArgumentParser(description="Stateful Anthropic Batch Inference Script")

# Workflow Flags
parser.add_argument("--prepare", action="store_true", help="Generate local .jsonl requests for Claude")
parser.add_argument("--debug", action="store_true", help="Process only instance 00 (Use with --prepare)")
parser.add_argument("--send", action="store_true", help="Send prepared requests to Claude Batch API")
parser.add_argument("--check", action="store_true", help="Check status of active batches")
parser.add_argument("--retrieve", action="store_true", help="Download results and reconstruct Excel files")
args = parser.parse_args()

NUM_OF_INSTANCES = 1 if args.debug else DEFAULT_NUM_INSTANCES

# put API key to `secrets/anthropic_api_key.txt`
# otherwise, use environment variables
API_KEY_PATH = os.path.join('secrets', 'anthropic_api_key.txt')
try:
    with open(API_KEY_PATH, 'r') as f:
        API_KEY = f.readline().strip()
    client = anthropic.Anthropic(api_key=API_KEY)
except:
    client = anthropic.Anthropic()

# ==========================================
# 3. WORKFLOW PIPELINE
# ==========================================

if args.prepare:
    print(f"\n{'='*60}\n[INFO] STAGE 1: PREPARING BATCH REQUESTS\n{'='*60}")
    
    if not os.path.exists(IMAGE_URLS_FILE):
        raise FileNotFoundError(f"Image URLs map not found at {IMAGE_URLS_FILE}. Run your drive crawler first.")
    with open(IMAGE_URLS_FILE, 'r', encoding='utf-8') as f:
        image_url_map = json.load(f)

    # Load User Prompt
    user_prompt_template = ""
    if os.path.exists(USER_PROMPT_PATH):
        with open(USER_PROMPT_PATH, "r", encoding="utf-8") as f:
            user_prompt_template = f.read().strip()
        print(f"[INFO] Loaded additional prompt template from {USER_PROMPT_PATH}")

    for model_name in MODELS:
        print(f"\n[INFO] Preparing Requests for Model: {model_name}")
        batch_requests = []
        
        for subject in SUBJECTS:
            for index in range(NUM_OF_INSTANCES):
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
                        # Create unique Custom ID
                        custom_id = f"{subject}||0{index}||{row['id']}||{lang_suffix}"
                        
                        # Reconstruct the precise local path to match the image_urls.json key
                        img_rel_path = row["image"].replace("\\", "/")
                        full_local_path = f"sample/0{index}/{subject}/{img_rel_path}"
                        img_url = image_url_map.get(full_local_path)
                        
                        if not img_url:
                            print(f"[!] Warning: No GDrive URL mapped for {full_local_path}. Skipping.")
                            continue

                        # Construct Final Text
                        base_desc = str(row[desc_col])
                        final_text = f"{base_desc}\n\n{user_prompt_template}" if user_prompt_template else base_desc

                        # Claude Parameter Config
                        params = {
                            "model": model_name,
                            "max_tokens": MAX_TOKENS,
                            "temperature": TEMPERATURE,
                            "messages": [
                                {
                                    "role": "user",
                                    "content": [
                                        {
                                            "type": "image",
                                            "source": {
                                                "type": "url",
                                                "url": img_url
                                            }
                                        },
                                        {
                                            "type": "text",
                                            "text": final_text
                                        }
                                    ]
                                }
                            ]
                        }
                        
                        # Inject thinking configuration if enabled
                        if ENABLE_THINKING:
                            params["thinking"] = {"type": "enabled", "budget_tokens": 4096}
                            params["temperature"] = 1.0 # Anthropic strictly requires temp=1.0 for thinking

                        # Anthropic JSONL Schema
                        request = {
                            "custom_id": custom_id,
                            "params": params
                        }
                        batch_requests.append(request)

        safe_model_name = model_name.replace("/", "_").replace(".", "_")
        jsonl_filename = os.path.join(CLAUDE_TEMP_DIR, f"req_{safe_model_name}.jsonl")
        
        with open(jsonl_filename, 'w', encoding='utf-8') as f:
            for req in batch_requests:
                # ensure_ascii=False handles Hindi, Arabic, Chinese, Kazakh properly
                f.write(json.dumps(req, ensure_ascii=False) + "\n")
        print(f"[INFO] Prepared {len(batch_requests)} requests -> {jsonl_filename}")


if args.send:
    print(f"\n{'='*60}\n[INFO] STAGE 2: SENDING BATCHES TO ANTHROPIC\n{'='*60}")
    
    batch_jobs = {}
    if os.path.exists(BATCH_JOBS_FILE):
        with open(BATCH_JOBS_FILE, 'r') as f:
            batch_jobs = json.load(f)

    for model_name in MODELS:
        safe_model_name = model_name.replace("/", "_").replace(".", "_")
        jsonl_filename = os.path.join(CLAUDE_TEMP_DIR, f"req_{safe_model_name}.jsonl")
        
        if not os.path.exists(jsonl_filename):
            print(f"[SKIP] No jsonl file found for {model_name}.")
            continue
            
        print(f"[INFO] Reading JSONL and sending to Anthropic Batch API for {model_name}...")
        
        # Anthropic SDK handles the file upload internally when passed an Iterable of dicts
        batch_requests = []
        with open(jsonl_filename, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    batch_requests.append(json.loads(line))
        
        try:
            # Support for both standard and beta SDK endpoints
            if hasattr(client.messages, "batches"):
                batch_job = client.messages.batches.create(requests=batch_requests)
            else:
                batch_job = client.beta.messages.batches.create(requests=batch_requests)
                
            batch_jobs[model_name] = {
                "batch_id": batch_job.id,
                "status": batch_job.processing_status
            }
            print(f"[SUCCESS] Submitted! Batch ID: {batch_job.id}")
            
        except Exception as e:
            print(f"[!] Error submitting batch for {model_name}: {e}")

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
        try:
            if hasattr(client.messages, "batches"):
                job_status = client.messages.batches.retrieve(job_info["batch_id"])
            else:
                job_status = client.beta.messages.batches.retrieve(job_info["batch_id"])
                
            state_str = job_status.processing_status
            batch_jobs[model_name]["status"] = state_str
            
            print(f"Model: {model_name.ljust(30)} | Status: {state_str.upper()}")
            
            if state_str.lower() != "ended":
                all_ready = False
        except Exception as e:
            print(f"[!] Error checking {model_name}: {e}")
            all_ready = False
            
    with open(BATCH_JOBS_FILE, 'w') as f:
        json.dump(batch_jobs, f, indent=4)
        
    print("\n------------------------------------------------------------")
    if all_ready:
        print("[READY] All batches are ended! You can now run with --retrieve")
    else:
        print("[WAIT] Batches are still processing. Check again later.")


if args.retrieve:
    print(f"\n{'='*60}\n[INFO] STAGE 4: RETRIEVING & SAVING RESULTS\n{'='*60}")
    
    if not os.path.exists(BATCH_JOBS_FILE):
        print("[!] No batches tracking file found to retrieve.")
        exit()
        
    with open(BATCH_JOBS_FILE, 'r') as f:
        batch_jobs = json.load(f)

    # Recap list to store failures
    retrieve_error_logs = []

    for model_name, job_info in batch_jobs.items():
        if str(job_info["status"]).lower() != "ended":
            log_msg = f"[SKIP] {model_name}: Status is '{job_info['status']}' (Needs to be 'ended')"
            print(log_msg)
            retrieve_error_logs.append(log_msg)
            continue
            
        print(f"\n[INFO] Retrieving results for {model_name}...")
        
        try:
            if hasattr(client.messages, "batches"):
                results_iter = client.messages.batches.results(job_info["batch_id"])
            else:
                results_iter = client.beta.messages.batches.results(job_info["batch_id"])
        except Exception as e:
            log_msg = f"[!] API Error retrieving results for {model_name}: {e}"
            print(log_msg)
            retrieve_error_logs.append(log_msg)
            continue
            
        mapped_results = {}
        error_count = 0
        
        # Anthropic's results() method returns an iterator of objects natively
        for res_obj in results_iter:
            # Convert the Pydantic model to a standard dictionary
            res = res_obj.model_dump()
            
            custom_id = res.get('custom_id', 'UNKNOWN||UNKNOWN||UNKNOWN||UNKNOWN')
            subj, idx_str, row_id, lang = custom_id.split("||")
            
            result_data = res.get('result', {})
            
            # Check if the individual request succeeded
            if result_data.get('type') == 'succeeded':
                try:
                    content_blocks = result_data.get('message', {}).get('content', [])
                    answer_parts = []
                    
                    for block in content_blocks:
                        # Skip thinking blocks natively handled by Anthropic's block types
                        if block.get('type') == 'text':
                            answer_parts.append(block.get('text', ''))
                            
                    if answer_parts:
                        answer = "\n".join(answer_parts).strip()
                    else:
                        answer = "[NO TEXT IN RESPONSE]"
                        error_count += 1
                        retrieve_error_logs.append(f"[{model_name}] No text block for {custom_id}")
                except Exception as e:
                    answer = "[ERROR EXTRACTING RESPONSE]"
                    error_count += 1
                    retrieve_error_logs.append(f"[{model_name}] Failed extraction for {custom_id}: {str(e)}")
            else:
                # If Anthropic's content filter tripped or the request was invalid
                answer = f"[API ERROR] {result_data.get('type')}"
                error_count += 1
                retrieve_error_logs.append(f"[{model_name}] API Error for {custom_id}: {result_data}")
                
            if subj not in mapped_results: mapped_results[subj] = {}
            if idx_str not in mapped_results[subj]: mapped_results[subj][idx_str] = {}
            if row_id not in mapped_results[subj][idx_str]: mapped_results[subj][idx_str][row_id] = {}
            
            mapped_results[subj][idx_str][row_id][lang] = answer

        if error_count > 0:
            print(f"[!] Warning: {error_count} responses failed to generate correctly.")

        # Reconstruct DataFrames & Export to Excel
        safe_model_name = model_name.replace("/", "_").replace(".", "_")
        
        for subject in SUBJECTS:
            for index in range(NUM_OF_INSTANCES):
                idx_str = f"0{index}"
                
                # Skip if no data was returned for this subject/instance combo
                if subject not in mapped_results or idx_str not in mapped_results[subject]:
                    continue
                    
                dataset_path = os.path.join("sample", idx_str, subject)
                json_path = os.path.join(dataset_path, 'dataset.json')
                
                if not os.path.exists(json_path): continue
                with open(json_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    
                df = pd.DataFrame.from_dict(data, orient="index")
                df.insert(0, "id", range(1, len(df) + 1))
                
                desc_columns = [col for col in df.columns if col.startswith("description")]
                for desc_col in desc_columns:
                    lang_key = desc_col.replace("description", "response") 
                    
                    df[lang_key] = df["id"].apply(
                        lambda r_id: mapped_results[subject][idx_str].get(str(r_id), {}).get(lang_key, "")
                    )

                output_path = os.path.join('result', 'raw', subject, idx_str)
                os.makedirs(output_path, exist_ok=True)
                full_output_path = os.path.join(output_path, f"{safe_model_name}.xlsx")
                
                df.to_excel(full_output_path, index=False, engine="openpyxl")
                print(f"[SUCCESS] Saved Excel -> {full_output_path}")

    # Write recap logs if any failures occurred
    if retrieve_error_logs:
        log_path = os.path.join(CLAUDE_TEMP_DIR, "retrieve_failures.log")
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write("=== RETRIEVE FAILURES LOG ===\n")
            for log_msg in retrieve_error_logs:
                f.write(log_msg + "\n")
        print(f"\n[INFO] Failure recap saved to {log_path}")

print("\n[INFO] Execution Finished.")