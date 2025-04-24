import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from bot.config import SERVICE_ACCOUNT_FILE

# Put your actual folder ID here
TARGET_FOLDER_ID = "1-1NLsU2E1OWpGPceksp_xeOz0q6SH8Nk"

def init_drive():
    gauth = GoogleAuth()
    gauth.ServiceAuth()
    return GoogleDrive(gauth)

def upload_to_gdrive(drive, file_path):
    filename = os.path.basename(file_path)
    gfile = drive.CreateFile({
        'title': filename,
        'parents': [{'id': TARGET_FOLDER_ID}]
    })
    gfile.SetContentFile(file_path)
    gfile.Upload()
    print(f"[GDRIVE] Uploaded: {filename} to folder {TARGET_FOLDER_ID}")
