import os
import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import MessageMediaDocument
from bot.config import API_ID, API_HASH, STRING_SESSION, CHANNEL_ID, DOWNLOAD_PATH, FROM_ID, TO_ID
from bot.gdrive import init_drive, upload_to_gdrive

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

async def process_messages(from_id=None, to_id=None):
    os.makedirs(DOWNLOAD_PATH, exist_ok=True)
    drive = init_drive()
    async for message in client.iter_messages(CHANNEL_ID, min_id=(from_id - 1) if from_id else None, max_id=to_id):
        if message.media and isinstance(message.media, MessageMediaDocument):
            try:
                file_path = await client.download_media(message, DOWNLOAD_PATH)
                print(f"[DOWNLOAD] {file_path}")
                upload_to_gdrive(drive, file_path)
            except Exception as e:
                print(f"[ERROR] {e}")

def main():
    print(f"Downloading messages from {FROM_ID} to {TO_ID}")
    with client:
        client.loop.run_until_complete(process_messages(FROM_ID, TO_ID))

if __name__ == "__main__":
    main()
