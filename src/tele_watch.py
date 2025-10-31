from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()

API_ID=os.environ.get("API_ID")
API_HASH=os.environ.get("API_HASH")

with TelegramClient('sesh',API_ID,API_HASH) as client:
    client.loop.run_until_complete(client.send_message('me',"Testing Connection"))
