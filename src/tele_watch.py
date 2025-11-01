from telethon import TelegramClient, events
from dotenv import load_dotenv
import requests
import logging
import asyncio
import os

########################
# Function Definitions #
########################
async def send_message_to_slack(text):
    payload={"text":text}
    try:
        response=requests.post(webhook,json=payload)
        response.raise_for_status()
        logger.info(f"##### Slack message delivered ####")
    except requests.RequestException as e:
        logger.error(f"Error sending message {e}")

async def
load_dotenv()

API_ID=os.environ.get('API_ID')
API_HASH=os.environ.get('API_HASH')
WEBHOOK=os.environ.get('webhook')
channels=['channel_1','channel_2']

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger=logging.getLogger(__name__)

async def main():
    client=TelegramClient('anon',API_ID,API_HASH)

    await client.start()
    channel_entities=await asyncio.gather(*(client.get_entity("channel") for channel in channels))

    @client.on(events.NewMessage)
    async def handle_message(event):
        sender=await event.get_sender()
        channel=await event.get_chat()
        message=event.raw_text

        text=f"Telegram Alert\nChannel: {(channel.title)}\nUser: {sender.username}\nMessage: {message}\n"
        logger.info(f"Message received from {sender.username} in {channel.title}: {message}")
        await send_message_to_slack(text)
    await client.run_until_disconnected()
    return handle_message
asyncio.run(main())



