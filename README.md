# Snapchat Memory Downloader

Recently, Snapchat introduced a **5GB limit on Memories**, so if you want a complete backup of all your memories, you need to download your data manually. This Python script helps you download all your Snapchat memories from a JSON export.  

As seen on: https://www.tiktok.com/@giraintech/video/7583879890265558280

---

## Getting Your Snapchat Data
1. Open Snapchat and go to Settings → My Data.
2. Request your Memories and select JSON formatting.
3. Snapchat will email you a link to download a ZIP file containing your exported data.
4. Extract the ZIP file and locate the JSON file to use with this script.

## How It Works

1. Export/Download your Snapchat memories as a JSON file from Snapchat.
2. Run the script in your terminal:

```bash
python3 download_snapchat.py
```

3. When prompted: Drag your memories_history.json file into the terminal. Press Enter.
4. When prompted: Drag the folder where you want your memories saved. Press Enter.
5. That’s it. The download will start automatically!


## Requirements
- Python 3.x
- Internet connection (to download media files)
- urllib (comes with Python standard library)
- Access to the JSON export from Snapchat

## Troubleshooting
### ❌ “File not found” error

Cause: The JSON path is wrong
Fix: Drag the file directly into the terminal — don’t type the path manually.

### ❌ JSONDecodeError

Cause: You selected the wrong file
Fix: Make sure the file is called:

memories_history.json

Not a folder, not a ZIP, not an HTML file.

### ❌ HTTP Error 403: Forbidden

This is normal and expected.

Snapchat download links expire after some time and can only be used a limited number of times so if you are running this program a bit after downloading the json. You might need to re-export a new json from Snapchat. Re-run the code and use the new memories_history.json


