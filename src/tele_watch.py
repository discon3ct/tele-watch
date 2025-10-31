from telethon import TelegramClient, events
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

API_ID=os.environ.get("API_ID")
API_HASH=os.environ.get("API_HASH")

async def main():
    client=TelegramClient('sesh',API_ID,API_HASH)

    @client.on(events.NewMessage)
    async def handle_message(event):
        print(event.message.text)

    await client.start()
    await client.run_until_disconnected()
    
    return handle_message

asyncio.run(main())



