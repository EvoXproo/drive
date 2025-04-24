# Telegram GDrive Bot

This bot downloads all files from a specified Telegram channel using Telethon and uploads them to Google Drive using a service account.

## Setup

1. Clone the repo or extract the zip.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Add your `service_account.json` to the root directory.
4. Configure `bot/config.py` with your credentials and channel ID.
5. Run the bot:
   ```
   python3 -m bot.main
   ```

## How To Create GDrive Service Account 


---

## Step 1: Google Cloud Console pe jao

Link : https://console.cloud.google.com/


---

## Step 2: Ek project banao ya existing select karo

Top bar me project selector pe click karo.

“New Project” select karo (ya koi existing project use karo).

Project ka naam do aur create karo.



---

## Step 3: Drive API enable karo

1. Left menu me jao: "APIs & Services" > "Library"


2. Search karo: Google Drive API


3. Click karo “Google Drive API”


4. Click “Enable”




---

## Step 4: Service account banao (first time only)

1. Go to: IAM & Admin > Service Accounts


2. Click "Create Service Account"

Name: e.g., drive-bot

Role: Editor or specifically Drive API > Drive File



3. Click Done


4. Us service account pe click karo > "Keys" tab me jao


5. Add Key > Create new key > JSON

Ye JSON file download hogi — isse aap service_account.json naam se bot folder me daal do.





---

## Step 5: Apne Google Drive pe access do

1. Drive kholke ek folder banao (optional).


2. Folder pe right-click > Share


3. Usme service account ka email daalo (e.g., xyz@projectid.iam.gserviceaccount.com)


4. Permission: Editor




---






































