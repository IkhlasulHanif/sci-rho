import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# --- USER CONFIGURATION ---
GDRIVE_FOLDER_ID_PATH = os.path.join('secrets', 'gdrive_folder_id.txt')
with open(GDRIVE_FOLDER_ID_PATH, 'r') as f:
    GDRIVE_FOLDER_ID = f.readline().strip()
IMAGE_TEMP_DIR = "image_temp"
IMAGE_URLS_FILE = os.path.join(IMAGE_TEMP_DIR, "image_urls.json")

SCOPES = ['https://www.googleapis.com/auth/drive']
# --------------------------

os.makedirs(IMAGE_TEMP_DIR, exist_ok=True)

# ==========================================
# 1. GOOGLE DRIVE AUTH & HELPERS
# ==========================================
def get_gdrive_service():
    """Handles Google Drive Authentication."""
    credentials_path = os.path.join("secrets", "token.json")
    flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
    creds = flow.run_local_server(port=0)
    return build('drive', 'v3', credentials=creds)

def find_folder_in_drive(service, parent_id, folder_name):
    """Searches for a specific folder inside a parent folder."""
    query = f"'{parent_id}' in parents and name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get('files', [])
    return files[0]['id'] if files else None

def crawl_folder_recursive(service, folder_id, current_path, url_map):
    """Recursively crawls Google Drive folders to map image URLs."""
    page_token = None
    while True:
        query = f"'{folder_id}' in parents and trashed = false"
        results = service.files().list(
            q=query, 
            pageSize=1000, 
            pageToken=page_token,
            fields="nextPageToken, files(id, name, mimeType)"
        ).execute()
        
        items = results.get('files', [])
        for item in items:
            # Construct the local path equivalent (e.g., "sample/00/physics/image/image1.png")
            item_path = f"{current_path}/{item['name']}"
            
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                # If it's a folder, dive deeper
                crawl_folder_recursive(service, item['id'], item_path, url_map)
            elif item['mimeType'].startswith('image/'):
                # If it's an image, map the direct download URL
                url_map[item_path] = f"https://drive.google.com/uc?id={item['id']}"
        
        page_token = results.get('nextPageToken', None)
        if page_token is None:
            break

# ==========================================
# 2. WORKFLOW PIPELINE
# ==========================================
if __name__ == "__main__":
    print("\n--- CRAWL & SAVE GOOGLE DRIVE URLS ---")
    
    service = get_gdrive_service()
    
    print(f"[*] Looking for 'sample' folder inside GDrive parent {GDRIVE_FOLDER_ID}...")
    sample_folder_id = find_folder_in_drive(service, GDRIVE_FOLDER_ID, "sample")
    
    if not sample_folder_id:
        print("[!] Error: Could not find the 'sample' folder in your Google Drive.")
        print(f"[!] Please ensure you uploaded a folder named 'sample' inside the folder ID: {GDRIVE_FOLDER_ID}")
        exit(1)
        
    print("[*] Found the 'sample' folder! Ensuring permissions are set to public reader...")
    try:
        # Applying read permissions to the parent folder so the images inherit it
        permission = {'type': 'anyone', 'role': 'reader'}
        service.permissions().create(fileId=sample_folder_id, body=permission).execute()
    except Exception as e:
        print(f"[!] Warning: Could not set public permissions automatically: {e}")
        
    print("[*] Crawling nested folders to map image URLs (this might take a minute)...")
    url_map = {}
    
    # Start the crawl using "sample" as the base path so it perfectly matches local paths
    crawl_folder_recursive(service, sample_folder_id, "sample", url_map)
    
    with open(IMAGE_URLS_FILE, 'w') as f:
        json.dump(url_map, f, indent=4)
        
    print(f"\n[SUCCESS] Mapped {len(url_map)} images!")
    print(f"[*] Saved to {IMAGE_URLS_FILE}. You can now run your eval gpt/gemini/claude/openrouter scripts!")