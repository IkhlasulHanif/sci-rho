import os
import json
import math
import shutil
from argparse import ArgumentParser
from pathlib import Path
from PIL import Image
from tqdm import tqdm
from huggingface_hub import HfApi

# --- USER CONFIGURATION ---
EXPERIMENT_ROOT = Path(__file__).resolve().parents[1]
IMAGE_TEMP_DIR = str(EXPERIMENT_ROOT / "image_temp")

# Resize Configuration
TARGET_IMAGE_PIXELS = 640 * 640  # Reference target total pixels (adjustable)
# --------------------------

os.makedirs(IMAGE_TEMP_DIR, exist_ok=True)
os.makedirs(EXPERIMENT_ROOT / 'secrets', exist_ok=True)


def get_mode_paths():
    return {
        "base_folder": "sample",
        "original_folder": "sample_original",
        "image_urls_file": os.path.join(IMAGE_TEMP_DIR, "image_urls.json"),
    }

# ==========================================
# 1. HF SECRETS LOADER
# ==========================================
def get_hf_credentials():
    """Loads HF token and repo ID from secrets to keep them hidden."""
    token_path = EXPERIMENT_ROOT / 'secrets' / 'hf_token.txt'
    repo_path = EXPERIMENT_ROOT / 'secrets' / 'hf_repo_id.txt'
    
    if not os.path.exists(token_path) or not os.path.exists(repo_path):
        print("[!] Error: Missing Hugging Face credentials.")
        print(f"    Please ensure '{token_path}' contains your HF Write Token.")
        print(f"    Please ensure '{repo_path}' contains your target dataset repo (e.g. 'username/dataset-name').")
        exit(1)
        
    with open(token_path, 'r') as f:
        token = f.read().strip()
    with open(repo_path, 'r') as f:
        repo_id = f.read().strip()
        
    return token, repo_id

# ==========================================
# 2. IMAGE RESIZING HELPERS
# ==========================================
def resize_local_images(base_folder="sample", original_folder="sample_original", target_pixels=TARGET_IMAGE_PIXELS):
    """Backs up the folder and resizes images to maintain aspect ratio while matching target total pixels."""
    base_folder = str(EXPERIMENT_ROOT / base_folder)
    original_folder = str(EXPERIMENT_ROOT / original_folder)
    if not os.path.exists(base_folder):
        print(f"[!] Error: The folder '{base_folder}' does not exist locally.")
        return

    # 1. Safely duplicate to sample_original
    if not os.path.exists(original_folder):
        print(f"[*] Backing up '{base_folder}' to '{original_folder}'...")
        shutil.copytree(base_folder, original_folder)
        print("[SUCCESS] Backup complete.")
    else:
        print(f"[*] Backup folder '{original_folder}' already exists. Proceeding with resize...")

    # 2. Gather all image files from the active 'sample' folder
    image_files = []
    for root, _, files in os.walk(base_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_files.append(os.path.join(root, file))
                
    if not image_files:
        print(f"[*] No images found in '{base_folder}'.")
        return

    print(f"[*] Found {len(image_files)} images. Resizing to ~{target_pixels} pixels...")
    
    resized_count = 0
    skipped_count = 0
    
    for img_path in tqdm(image_files, desc="Resizing Images", unit="img"):
        try:
            with Image.open(img_path) as img:
                w, h = img.size
                current_pixels = w * h
                
                if current_pixels == 0:
                    continue
                    
                # Calculate scale factor to match target pixels
                scale_factor = math.sqrt(target_pixels / current_pixels)
                
                new_w = max(1, int(w * scale_factor))
                new_h = max(1, int(h * scale_factor))
                
                # Idempotency check: only resize if the dimensions actually change
                if new_w == w and new_h == h:
                    skipped_count += 1
                    continue
                    
                # Resampling.LANCZOS provides high-quality downsampling/upsampling
                # Fallback to Image.LANCZOS for older Pillow versions
                resample_filter = getattr(Image, 'Resampling', Image).LANCZOS
                resized_img = img.resize((new_w, new_h), resample_filter)
                
            # Overwrite the active image in place (since we backed up original)
            resized_img.save(img_path)
            resized_count += 1
            
        except Exception as e:
            print(f"\n[!] Error processing {img_path}: {e}")
            
    print(f"\n[SUCCESS] Resize complete! Resized: {resized_count}, Skipped (already correct): {skipped_count}")

# ==========================================
# 3. HUGGING FACE HELPERS
# ==========================================
def upload_to_huggingface(local_folder="sample"):
    """Uploads the local folder to a Hugging Face Dataset repository."""
    token, repo_id = get_hf_credentials()
    api = HfApi(token=token)
    local_folder = str(EXPERIMENT_ROOT / local_folder)
    
    print(f"[*] Uploading '{local_folder}' to Hugging Face repo '{repo_id}'...")
    try:
        # Check if repo exists, create if not (creates a Dataset repo)
        api.create_repo(repo_id=repo_id, repo_type="dataset", exist_ok=True)
        
        # Upload folder
        api.upload_large_folder(
            folder_path=local_folder,
            repo_id=repo_id,
            repo_type="dataset",
            ignore_patterns=["~$*"],
        )
        print("[SUCCESS] Folder successfully uploaded to Hugging Face!")
    except Exception as e:
        print(f"[!] Error uploading to Hugging Face: {e}")

def get_huggingface_urls(image_urls_file):
    """Crawls the Hugging Face repo to map direct image URLs and deletes all non-image files."""
    token, repo_id = get_hf_credentials()
    api = HfApi(token=token)
    
    print(f"[*] Fetching file list from Hugging Face repo '{repo_id}'...")
    try:
        # List all files in the repository
        files = api.list_repo_files(repo_id=repo_id, repo_type="dataset")
    except Exception as e:
        print(f"[!] Error fetching file list: {e}")
        return

    url_map = {}
    files_to_delete = []
    
    valid_extensions = ('.png', '.jpg', '.jpeg')
    # Protected files that Hugging Face uses under the hood; safe to ignore during deletion
    protected_files = ('.gitattributes', 'readme.md')

    # Filter and construct direct resolve URLs, and collect non-image files
    for file_path in tqdm(files, desc="Scanning files", unit="file"):
        file_lower = file_path.lower()
        
        if file_lower.endswith(valid_extensions):
            # Construct the direct raw download URL
            direct_url = f"https://huggingface.co/datasets/{repo_id}/resolve/main/{file_path}"
            url_map[file_path] = direct_url
        elif not file_lower.endswith(protected_files):
            # If it is not an image and not a protected repo file, mark for deletion
            files_to_delete.append(file_path)

    # Process deletions if any non-image files were found
    if files_to_delete:
        print(f"\n[*] Found {len(files_to_delete)} non-image files (e.g., .xlsx, .json). Deleting from repository...")
        for file_to_del in tqdm(files_to_delete, desc="Deleting files", unit="file"):
            try:
                api.delete_file(
                    path_in_repo=file_to_del,
                    repo_id=repo_id,
                    repo_type="dataset",
                    commit_message=f"Cleanup: Delete non-image file {file_to_del}"
                )
            except Exception as e:
                print(f"\n[!] Error deleting {file_to_del}: {e}")
            
    # SAFETY MECHANISM: Check before replacing mapping file
    if os.path.exists(image_urls_file):
        print(f"\n[!] Safety Check: '{image_urls_file}' already exists. Skipping save to prevent overwrite.")
        print("[INFO] If you want to update the URLs, please delete or rename the existing file first.")
    else:
        with open(image_urls_file, 'w') as f:
            json.dump(url_map, f, indent=4)
        print(f"\n[SUCCESS] Successfully mapped a total of {len(url_map)} images!")
        print(f"[*] Saved to {image_urls_file}. You can now run your eval scripts!")


# ==========================================
# 4. WORKFLOW PIPELINE
# ==========================================
def main():
    parser = ArgumentParser(description="Manage Image Resizing and Hugging Face Syncing")
    parser.add_argument("--resize", action="store_true", help="Backup and resize local images in the selected sample folder")
    parser.add_argument("--upload", action="store_true", help="Upload the selected sample folder to Hugging Face")
    parser.add_argument("--get", action="store_true", help="Get URLs from Hugging Face and map to json")
    args = parser.parse_args()
    paths = get_mode_paths()

    if not args.resize and not args.upload and not args.get:
        print("Please specify at least one flag: --resize, --upload, and/or --get")
        parser.print_help()
        exit(0)

    # 1. Execute Resize Block
    if args.resize:
        print("\n--- STAGE 1: RESIZE LOCAL IMAGES ---")
        resize_local_images(
            base_folder=paths["base_folder"],
            original_folder=paths["original_folder"],
        )

    # 2. Execute HF Upload Block
    if args.upload:
        print("\n--- STAGE 2: UPLOAD TO HUGGING FACE ---")
        upload_to_huggingface(local_folder=paths["base_folder"])

    # 3. Execute HF URL Mapping Block
    if args.get:
        print("\n--- STAGE 3: GET HUGGING FACE URLS ---")
        get_huggingface_urls(paths["image_urls_file"])


if __name__ == "__main__":
    main()
