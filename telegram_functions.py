# telegram_functions.py
import os
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaDocument
from telethon.errors import FloodWaitError
import asyncio






async def search_videos(client, phone_number, chat_id, word1=None, word2=None, limit=None, forward_to_saved=True):
    """
    Search for video files in a specified chat and optionally forward them to saved messages.
    """
    await client.start(phone=phone_number)
    word1 = word1.lower() if word1 else ""
    word2 = word2.lower() if word2 else ""
    video_messages = []
    
    print("Starting search...")  # Debug output
    
    async for message in client.iter_messages(chat_id, limit=limit):
        if message.media and isinstance(message.media, MessageMediaDocument):
            if message.media.document.mime_type.startswith('video/'):
                video_file_name = None
                for attr in message.media.document.attributes:
                    if hasattr(attr, 'file_name'):
                        video_file_name = attr.file_name
                        break
                if video_file_name:
                    if word1 in video_file_name.lower() and word2 in video_file_name.lower():
                        video_messages.append((message, video_file_name))
                        if forward_to_saved:
                            try:
                                await client.forward_messages('me', message)
                                print(f"Forwarded video: {video_file_name}")  # Debug output
                            except FloodWaitError as e:
                                print(f"Flood wait error: Wait for {e.seconds} seconds before retrying.")
                                await asyncio.sleep(e.seconds)
                            except Exception as e:
                                print(f"Error: {e}")
    
    print(f"Found {len(video_messages)} videos.")  # Debug output
    return video_messages
