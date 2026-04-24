import os
import json
import pandas as pd
import time
from tqdm import tqdm
from argparse import ArgumentParser
from google import genai

# ==========================================
# 1. USER CONFIGURATION
# ==========================================
# Paths & Directories
GEMINI_TEMP_DIR = "gemini_temp"
GEMINI_UPLOADED_IMAGES_FILE = os.path.join(GEMINI_TEMP_DIR, "gemini_uploaded_images.json")
BATCH_JOBS_FILE = os.path.join(GEMINI_TEMP_DIR, "batch_jobs.json")
ERROR_BATCH_JOBS_FILE = os.path.join(GEMINI_TEMP_DIR, "error_batch_jobs.json")
USER_PROMPT_PATH = "user_prompt.txt"

# Experiment Scope
MODELS = [
    "gemini-2.5-flash", 
    "gemini-2.5-pro", 
    # "gemini-2.5-flash-lite" # for debugging only
]
SUBJECTS = [
    "mathematics", 
    "physics", 
    "chemistry", 
    "biology", 
    "compsci"
]
DEFAULT_NUM_INSTANCES = 10

# Sampling Parameters
TEMPERATURE = 0.0
MAX_TOKENS_FLASH = 4096
MAX_TOKENS_PRO = 8192
THINKING_BUDGET_FLASH = 0
THINKING_BUDGET_PRO = 2048

os.makedirs(GEMINI_TEMP_DIR, exist_ok=True)

# ==========================================
# 2. ARGUMENT PARSING
# ==========================================
parser = ArgumentParser(description="Stateful Gemini Batch Inference Script")

# Workflow Flags
parser.add_argument("--upload_image", action="store_true", help="Upload local images to Gemini Files API")
parser.add_argument("--prepare", action="store_true", help="Generate local .jsonl requests for Gemini")
parser.add_argument("--debug", action="store_true", help="Process only instance 00 (Use with --prepare)")
parser.add_argument("--send", action="store_true", help="Send prepared .jsonl requests to Gemini Batch API")
parser.add_argument("--check", action="store_true", help="Check status of active batches")
parser.add_argument("--retrieve", action="store_true", help="Download results and reconstruct Excel files")

# Error Handling Flags
parser.add_argument("--error_prepare", action="store_true", help="Parse request logs and prepare jsonl for failed instances")
parser.add_argument("--error_send", action="store_true", help="Send the error-specific jsonl to Gemini Batch API")
parser.add_argument("--error_check", action="store_true", help="Check status of error batches")
parser.add_argument("--error_retrieve", action="store_true", help="Download error results and strictly patch Excel files")
args = parser.parse_args()

NUM_OF_INSTANCES = 1 if args.debug else DEFAULT_NUM_INSTANCES

# put API key to `secrets/gemini_api_key.txt`
# otherwise, use environment variables
API_KEY_PATH = os.path.join('secrets', 'gemini_api_key.txt')
try:
    with open(API_KEY_PATH, 'r') as f:
        API_KEY = f.readline().strip()
    client = genai.Client(api_key=API_KEY)
except:
    client = genai.Client()

# ==========================================
# 3. WORKFLOW PIPELINE
# ==========================================

if args.upload_image:
    print(f"\n{'='*60}\n[INFO] STAGE 0: UPLOADING IMAGES TO GEMINI\n{'='*60}")
    
    uploaded_map = {}
    if os.path.exists(GEMINI_UPLOADED_IMAGES_FILE):
        with open(GEMINI_UPLOADED_IMAGES_FILE, 'r', encoding='utf-8') as f:
            uploaded_map = json.load(f)
            
    upload_count = 0
    current_time = time.time()
    
    for subject in SUBJECTS:
        for index in range(NUM_OF_INSTANCES):
            dataset_path = os.path.join("sample", f"0{index}", subject)
            json_path = os.path.join(dataset_path, 'dataset.json')
            
            if not os.path.exists(json_path): continue
            with open(json_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            df = pd.DataFrame.from_dict(data, orient="index")
            if len(df) == 0: continue
            
            for _, row in tqdm(df.iterrows(), total=len(df), desc=f"Uploading {subject}-0{index}", leave=False):
                if "image" not in row or pd.isna(row["image"]): continue
                
                img_rel_path = str(row["image"]).replace("\\", "/")
                full_local_path = f"sample/0{index}/{subject}/{img_rel_path}"
                map_key = f"0{index}/{subject}/{img_rel_path}" # Excludes 'sample/' prefix
                
                # Skip if we've already uploaded this exact file and it hasn't expired (45h buffer)
                skip_upload = False
                if map_key in uploaded_map:
                    val = uploaded_map[map_key]
                    if isinstance(val, dict) and "timestamp" in val:
                        if (current_time - val["timestamp"]) <= 45 * 3600:
                            skip_upload = True
                
                if skip_upload:
                    continue
                    
                if os.path.exists(full_local_path):
                    try:
                        myfile = client.files.upload(file=full_local_path)
                        # Save the Gemini URI and timestamp as the identifier for the API
                        uploaded_map[map_key] = {
                            "uri": myfile.uri,
                            "timestamp": time.time()
                        }
                        upload_count += 1
                    except Exception as e:
                        print(f"\n[!] Failed to upload {full_local_path}: {e}")
                else:
                    print(f"\n[!] Image not found locally: {full_local_path}")
                    
    # Save the mapping file
    with open(GEMINI_UPLOADED_IMAGES_FILE, 'w', encoding='utf-8') as f:
        json.dump(uploaded_map, f, indent=4)
        
    print(f"\n[INFO] Uploaded {upload_count} new images. Total mapped: {len(uploaded_map)}")
    print(f"[*] Mapping safely saved to {GEMINI_UPLOADED_IMAGES_FILE}")


if args.prepare:
    print(f"\n{'='*60}\n[INFO] STAGE 1: PREPARING BATCH REQUESTS\n{'='*60}")
    
    if not os.path.exists(GEMINI_UPLOADED_IMAGES_FILE):
        raise FileNotFoundError(f"Gemini image map not found at {GEMINI_UPLOADED_IMAGES_FILE}. Run --upload_image first.")
    with open(GEMINI_UPLOADED_IMAGES_FILE, 'r', encoding='utf-8') as f:
        image_url_map = json.load(f)

    # Validate 45-hour expiration constraint
    current_time = time.time()
    for key, val in image_url_map.items():
        if not isinstance(val, dict) or "timestamp" not in val or "uri" not in val:
            print("[!] Error: Legacy image mapping detected without timestamps. Please re-run --upload_image.")
            exit(1)
        if current_time - val["timestamp"] > 45 * 3600:
            print(f"[!] Error: Uploaded images are older than 45 hours. Gemini files expire in 48 hours. Please re-run --upload_image.")
            exit(1)

    # Load User Prompt
    user_prompt_template = ""
    if os.path.exists(USER_PROMPT_PATH):
        with open(USER_PROMPT_PATH, "r", encoding="utf-8") as f:
            user_prompt_template = f.read().strip()
        print(f"[INFO] Loaded additional prompt template from {USER_PROMPT_PATH}")

    for model_name in MODELS:
        if model_name=='gemini-2.5-flash':
            MAX_TOKENS = MAX_TOKENS_FLASH
            THINKING_BUDGET = THINKING_BUDGET_FLASH
        else:
            MAX_TOKENS = MAX_TOKENS_PRO
            THINKING_BUDGET = THINKING_BUDGET_PRO
        safe_model_name = model_name.replace("/", "_").replace(".", "_")
        jsonl_filename = os.path.join(GEMINI_TEMP_DIR, f"req_{safe_model_name}.jsonl")
        
        # Safety Check: Do not overwrite existing preparation files
        if os.path.exists(jsonl_filename):
            print(f"[!] Safety Check: '{jsonl_filename}' already exists. Skipping preparation for {model_name}.")
            continue

        print(f"\n[INFO] Preparing Requests for Model: {model_name}")
        batch_requests = []
        
        for subject in SUBJECTS:
            for index in range(NUM_OF_INSTANCES):
                # FIXED: Added "sample" back so it reads the local hard drive correctly
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
                    
                    for _, row in tqdm(df.iterrows(), total=len(df), desc=f"Preparing {subject}-0{index}", leave=False):
                        # Create unique Custom ID
                        custom_id = f"{subject}||0{index}||{row['id']}||{lang_suffix}"
                        
                        # Reconstruct the precise local path to match the new gemini uploaded map key
                        img_rel_path = row["image"].replace("\\", "/")
                        # FIXED: Exclude "sample/" here so it maps to the dictionary key
                        full_local_path = f"0{index}/{subject}/{img_rel_path}"
                        img_data = image_url_map.get(full_local_path)
                        
                        if not img_data:
                            print(f"\n[!] Warning: No URL mapped for {full_local_path}. Skipping.")
                            continue

                        img_url = img_data["uri"]

                        # Construct Final Text
                        base_desc = str(row[desc_col])
                        if user_prompt_template:
                            final_text = f"{base_desc}\n\n{user_prompt_template}"
                        else:
                            print("[!] ERROR: PROMPT TEMPLATE NOT FOUND")
                            exit()

                        # Simplified Gemini Config
                        generation_config = {
                            "temperature": TEMPERATURE,
                            "max_output_tokens": MAX_TOKENS,
                            "thinkingConfig": {
                                "thinkingBudget": THINKING_BUDGET
                            }
                        }

                        # Gemini JSONL Schema
                        request = {
                            "custom_id": custom_id,
                            "method": "generateContent",
                            "request": {
                                "contents": [
                                    {
                                        "role": "user",
                                        "parts": [
                                            # img_url is now the Gemini File URI we recorded
                                            {"file_data": {"file_uri": img_url, "mime_type": "image/png"}},
                                            {"text": final_text}
                                        ]
                                    }
                                ],
                                "generation_config": generation_config
                            }
                        }
                        batch_requests.append(request)
        
        with open(jsonl_filename, 'w', encoding='utf-8') as f:
            for req in batch_requests:
                # ensure_ascii=False handles Hindi, Arabic, Chinese, Kazakh properly
                f.write(json.dumps(req, ensure_ascii=False) + "\n")
        print(f"[INFO] Prepared {len(batch_requests)} requests -> {jsonl_filename}")


if args.send:
    print(f"\n{'='*60}\n[INFO] STAGE 2: SENDING BATCHES TO GEMINI\n{'='*60}")
    
    batch_jobs = {}
    if os.path.exists(BATCH_JOBS_FILE):
        with open(BATCH_JOBS_FILE, 'r') as f:
            batch_jobs = json.load(f)

    for model_name in MODELS:
        safe_model_name = model_name.replace("/", "_").replace(".", "_")
        jsonl_filename = os.path.join(GEMINI_TEMP_DIR, f"req_{safe_model_name}.jsonl")
        
        if not os.path.exists(jsonl_filename):
            print(f"[SKIP] No jsonl file found for {model_name}.")
            continue
            
        print(f"[INFO] Uploading file to Gemini API for {model_name}...")
        uploaded_file = client.files.upload(
            file=jsonl_filename,
            config={'mime_type': 'application/jsonl'}
        )
        
        print(f"[INFO] Triggering Batch API for {model_name}...")
        batch_job = client.batches.create(
            model=model_name,
            src=uploaded_file.name
        )
        
        # Extract state cleanly
        state_str = batch_job.state.name if hasattr(batch_job.state, 'name') else str(batch_job.state)
        batch_jobs[model_name] = {
            "batch_id": batch_job.name, # Gemini uses '.name' as the ID (e.g. 'batches/12345')
            "input_file_id": uploaded_file.name,
            "status": state_str
        }
        print(f"[SUCCESS] Submitted! Batch ID: {batch_job.name}")

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
        job_status = client.batches.get(name=job_info["batch_id"])
        state_str = job_status.state.name if hasattr(job_status.state, 'name') else str(job_status.state)
        batch_jobs[model_name]["status"] = state_str
        
        # Strip "JOB_STATE_" if present for cleaner printing
        clean_status = state_str.replace("JOB_STATE_", "").upper()
        print(f"Model: {model_name.ljust(30)} | Status: {clean_status}")
        
        if "SUCCEEDED" not in clean_status and "COMPLETED" not in clean_status:
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
        
        if "SUCCEEDED" not in str(job_info["status"]).upper():
            log_msg = f"[SKIP] {model_name}: Status is '{job_info['status']}' (Needs to be 'SUCCEEDED')"
            print(log_msg)
            continue
            
        print(f"\n[INFO] Retrieving results for {model_name}...")
        job_status = client.batches.get(name=job_info["batch_id"])
        
        try:
            remote_filename = job_status.dest.file_name
        except AttributeError:
            log_msg = f"[!] Warning: No output file generated for {model_name}"
            print(log_msg)
            request_logs.append(log_msg)
            
            if hasattr(job_status, 'error'):
                request_logs.append(f"[{model_name}] Error Details:\n{job_status.error}")
                
            # Save logs before continuing to the next model (Safety check removed)
            log_path = os.path.join(GEMINI_TEMP_DIR, f"{safe_model_name}_requests.log")
            with open(log_path, 'w', encoding='utf-8') as f:
                f.write(f"=== REQUEST LOGS FOR {model_name} ===\n")
                for msg in request_logs: f.write(msg + "\n")
            print(f"\n[INFO] Detailed request logs saved to {log_path}")
            continue
            
        # Download the JSONL output from Gemini
        content_bytes = client.files.download(file=remote_filename)
        result_content = content_bytes.decode('utf-8')
        
        # Structure: mapped_results[subject][instance_str][row_id_str][lang_suffix] = response_text
        mapped_results = {}
        error_count = 0
        
        raw_jsonl_path = os.path.join(GEMINI_TEMP_DIR, f"{safe_model_name}_raw_responses.jsonl")
        
        lines = result_content.strip().split('\n')
        with open(raw_jsonl_path, 'a', encoding='utf-8') as raw_f:
            for line in tqdm(lines, desc=f"Parsing {model_name}"):
                if not line: continue
                res = json.loads(line)
                
                # Dump the full JSON response into the aggregated JSONL file
                raw_f.write(json.dumps(res, ensure_ascii=False) + '\n')
                
                custom_id = res.get('custom_id', 'UNKNOWN||UNKNOWN||UNKNOWN||UNKNOWN')
                subj, idx_str, row_id, lang = custom_id.split("||")
                
                # Simplified Gemini Extraction Logic (No Thinking Bypass)
                if 'error' in res:
                    answer = f"[API ERROR] {res.get('error')}"
                    error_count += 1
                    request_logs.append(f"[{model_name}] FAILED  | ID: {custom_id} | API Error: {res.get('error')}")
                else:
                    try:
                        candidates = res.get('response', {}).get('candidates', [])
                        if candidates and 'content' in candidates[0]:
                            parts = candidates[0]['content'].get('parts', [])
                            # Grab all text parts safely
                            answer_parts = [p['text'] for p in parts if 'text' in p]
                            
                            if answer_parts:
                                answer = "\n".join(answer_parts).strip()
                                request_logs.append(f"[{model_name}] SUCCESS | ID: {custom_id}")
                            else:
                                answer = "[NO TEXT IN RESPONSE]"
                                error_count += 1
                                request_logs.append(f"[{model_name}] FAILED  | ID: {custom_id} | No text in response.")
                        else:
                            answer = "[NO CANDIDATES GENERATED]"
                            error_count += 1
                            request_logs.append(f"[{model_name}] FAILED  | ID: {custom_id} | No candidates generated.")
                    except Exception as e:
                        answer = "[ERROR EXTRACTING RESPONSE]"
                        error_count += 1
                        request_logs.append(f"[{model_name}] FAILED  | ID: {custom_id} | Exception: {str(e)}")
                    
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
                    
                # FIXED: Added "sample" back so it reads the local hard drive correctly
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
                
                # Safety Check: Do not overwrite existing Excel results
                if os.path.exists(full_output_path):
                    print(f"[!] Safety Check: '{full_output_path}' already exists. Skipping Excel save.")
                else:
                    df.to_excel(full_output_path, index=False, engine="openpyxl")
                    print(f"[SUCCESS] Saved Excel -> {full_output_path}")

        # Write detailed request logs for this model (Always overwrites)
        if request_logs:
            log_path = os.path.join(GEMINI_TEMP_DIR, f"{safe_model_name}_requests.log")
            with open(log_path, 'w', encoding='utf-8') as f:
                f.write(f"=== REQUEST LOGS FOR {model_name} ===\n")
                for log_msg in request_logs:
                    f.write(log_msg + "\n")
            print(f"\n[INFO] Detailed request logs saved to {log_path}")

# ==========================================
# 4. ERROR HANDLING PIPELINE
# ==========================================

if args.error_prepare:
    print(f"\n{'='*60}\n[INFO] ERROR STAGE 1: PREPARING FAILED REQUESTS\n{'='*60}")
    for model_name in MODELS:
        safe_model_name = model_name.replace("/", "_").replace(".", "_")
        log_path = os.path.join(GEMINI_TEMP_DIR, f"{safe_model_name}_requests.log")
        orig_jsonl = os.path.join(GEMINI_TEMP_DIR, f"req_{safe_model_name}.jsonl")
        error_jsonl = os.path.join(GEMINI_TEMP_DIR, f"req_{safe_model_name}_error.jsonl")

        if not os.path.exists(log_path) or not os.path.exists(orig_jsonl):
            continue

        failed_ids = set()
        with open(log_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Target format: [model_name] FAILED  | ID: physics||00||12||response_indonesian | ...
                if "FAILED" in line and "| ID: " in line:
                    try:
                        # Extract just the custom_id component
                        cid = line.split("| ID: ")[1].split(" |")[0].strip()
                        failed_ids.add(cid)
                    except:
                        pass

        if not failed_ids:
            print(f"[INFO] No failed requests found in logs for {model_name}.")
            continue

        error_reqs = []
        with open(orig_jsonl, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip(): continue
                req = json.loads(line)
                if req.get("custom_id") in failed_ids:
                    error_reqs.append(req)

        with open(error_jsonl, 'w', encoding='utf-8') as f:
            for req in error_reqs:
                f.write(json.dumps(req, ensure_ascii=False) + "\n")
        
        print(f"[INFO] Parsed {len(failed_ids)} failed IDs. Saved {len(error_reqs)} requests -> {error_jsonl}")

if args.error_send:
    print(f"\n{'='*60}\n[INFO] ERROR STAGE 2: SENDING FAILED BATCHES TO GEMINI\n{'='*60}")
    
    error_batch_jobs = {}
    if os.path.exists(ERROR_BATCH_JOBS_FILE):
        with open(ERROR_BATCH_JOBS_FILE, 'r') as f:
            error_batch_jobs = json.load(f)

    for model_name in MODELS:
        safe_model_name = model_name.replace("/", "_").replace(".", "_")
        error_jsonl = os.path.join(GEMINI_TEMP_DIR, f"req_{safe_model_name}_error.jsonl")
        
        if not os.path.exists(error_jsonl):
            print(f"[SKIP] No error jsonl file found for {model_name}.")
            continue
            
        print(f"[INFO] Uploading ERROR file to Gemini API for {model_name}...")
        uploaded_file = client.files.upload(
            file=error_jsonl,
            config={'mime_type': 'application/jsonl'}
        )
        
        print(f"[INFO] Triggering ERROR Batch API for {model_name}...")
        batch_job = client.batches.create(
            model=model_name,
            src=uploaded_file.name
        )
        
        state_str = batch_job.state.name if hasattr(batch_job.state, 'name') else str(batch_job.state)
        error_batch_jobs[model_name] = {
            "batch_id": batch_job.name,
            "input_file_id": uploaded_file.name,
            "status": state_str
        }
        print(f"[SUCCESS] Submitted! Error Batch ID: {batch_job.name}")

    with open(ERROR_BATCH_JOBS_FILE, 'w') as f:
        json.dump(error_batch_jobs, f, indent=4)

if args.error_check:
    print(f"\n{'='*60}\n[INFO] ERROR STAGE 3: CHECKING ERROR BATCH STATUS\n{'='*60}")
    
    if not os.path.exists(ERROR_BATCH_JOBS_FILE):
        print("[INFO] No active error batches found in tracking file.")
        exit()
        
    with open(ERROR_BATCH_JOBS_FILE, 'r') as f:
        error_batch_jobs = json.load(f)
        
    all_ready = True
    for model_name, job_info in error_batch_jobs.items():
        job_status = client.batches.get(name=job_info["batch_id"])
        state_str = job_status.state.name if hasattr(job_status.state, 'name') else str(job_status.state)
        error_batch_jobs[model_name]["status"] = state_str
        
        clean_status = state_str.replace("JOB_STATE_", "").upper()
        print(f"Model: {model_name.ljust(30)} | Status: {clean_status}")
        
        if "SUCCEEDED" not in clean_status and "COMPLETED" not in clean_status:
            all_ready = False
            
    with open(ERROR_BATCH_JOBS_FILE, 'w') as f:
        json.dump(error_batch_jobs, f, indent=4)
        
    print("\n------------------------------------------------------------")
    if all_ready:
        print("[READY] All error batches are completed! You can now run with --error_retrieve")
    else:
        print("[WAIT] Error batches are still processing. Check again later.")

if args.error_retrieve:
    print(f"\n{'='*60}\n[INFO] ERROR STAGE 4: RETRIEVING & PATCHING RESULTS\n{'='*60}")
    
    if not os.path.exists(ERROR_BATCH_JOBS_FILE):
        print("[!] No error batches tracking file found to retrieve.")
        exit()
        
    with open(ERROR_BATCH_JOBS_FILE, 'r') as f:
        error_batch_jobs = json.load(f)

    for model_name, job_info in error_batch_jobs.items():
        safe_model_name = model_name.replace("/", "_").replace(".", "_")
        
        if "SUCCEEDED" not in str(job_info["status"]).upper():
            print(f"[SKIP] {model_name}: Status is '{job_info['status']}'")
            continue
            
        print(f"\n[INFO] Retrieving error results for {model_name}...")
        job_status = client.batches.get(name=job_info["batch_id"])
        
        try:
            remote_filename = job_status.dest.file_name
        except AttributeError:
            print(f"[!] Warning: No output file generated for {model_name}")
            continue
            
        # Download the JSONL output from Gemini
        content_bytes = client.files.download(file=remote_filename)
        result_content = content_bytes.decode('utf-8')
        
        mapped_results = {}
        error_raw_jsonl = os.path.join(GEMINI_TEMP_DIR, f"{safe_model_name}_raw_responses_error.jsonl")
        
        lines = result_content.strip().split('\n')
        with open(error_raw_jsonl, 'a', encoding='utf-8') as raw_f:
            for line in tqdm(lines, desc=f"Parsing {model_name} Error Returns"):
                if not line: continue
                res = json.loads(line)
                
                raw_f.write(json.dumps(res, ensure_ascii=False) + '\n')
                
                custom_id = res.get('custom_id')
                if not custom_id: continue
                
                subj, idx_str, row_id, lang = custom_id.split("||")
                
                # Check if it finally succeeded
                if 'error' not in res:
                    try:
                        candidates = res.get('response', {}).get('candidates', [])
                        if candidates and 'content' in candidates[0]:
                            parts = candidates[0]['content'].get('parts', [])
                            answer_parts = [p['text'] for p in parts if 'text' in p]
                            
                            if answer_parts:
                                answer = "\n".join(answer_parts).strip()
                                # Load into mapped_results to trigger patching
                                if subj not in mapped_results: mapped_results[subj] = {}
                                if idx_str not in mapped_results[subj]: mapped_results[subj][idx_str] = {}
                                if row_id not in mapped_results[subj][idx_str]: mapped_results[subj][idx_str][row_id] = {}
                                
                                mapped_results[subj][idx_str][row_id][lang] = answer
                    except:
                        pass

        # Perform the actual strict patching of the existing .xlsx files
        patch_count = 0
        for subj, subj_data in mapped_results.items():
            for idx_str, idx_data in subj_data.items():
                excel_path = os.path.join('result', 'raw', subj, idx_str, f"{safe_model_name}.xlsx")
                if os.path.exists(excel_path):
                    try:
                        df = pd.read_excel(excel_path)
                        patched = False
                        
                        for row_id_str, lang_data in idx_data.items():
                            row_id_int = int(row_id_str)
                            for lang, answer in lang_data.items():
                                # Target the specific cell using boolean indexing
                                df.loc[df['id'] == row_id_int, lang] = answer
                                patched = True
                                patch_count += 1
                                
                        if patched:
                            df.to_excel(excel_path, index=False, engine="openpyxl")
                    except Exception as e:
                        print(f" [!] Failed to patch {excel_path}: {e}")
                        
        print(f" [SUCCESS] Safely patched {patch_count} cells into existing Excel files for {model_name}.")

print("\n[INFO] Execution Finished.")