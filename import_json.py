import json
import os
import urllib.request
from datetime import datetime
import ssl

print("📁 Drag your Snapchat memories_history.json file here and press Enter:")
JSON_FILE = input().strip().replace("\\", "")

print("📂 Drag the folder where you want downloads saved and press Enter:")
OUTPUT_DIR = input().strip().replace("\\", "")

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(JSON_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

media_items = data.get("Saved Media", [])

def build_filename(date_str, ext):
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S UTC")
    return dt.strftime("%Y-%m-%d_%H-%M-%S") + ext

existing_files = set(os.listdir(OUTPUT_DIR))

for item in media_items:
    media_type = item.get("Media Type", "").lower()
    ext = ".mp4" if media_type == "video" else ".jpg"

    date_str = item.get("Date")
    url = item.get("Media Download Url")

    if not date_str or not url:
        continue

    filename = build_filename(date_str, ext)
    filepath = os.path.join(OUTPUT_DIR, filename)

    # ✅ Skip if already downloaded
    if filename in existing_files:
        print(f"⏭️ Skipping existing file: {filename}")
        continue

    print(f"Downloading {filename} → {OUTPUT_DIR}")

    try:
        urllib.request.urlretrieve(url, filepath)
        existing_files.add(filename)
    except Exception as e:
        print(f"❌ Failed: {e}")

print("✅ All remaining Snapchat memories downloaded")
