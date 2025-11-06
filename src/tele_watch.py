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
        response=requests.post(WEBHOOK,json=payload)
        response.raise_for_status()
        logger.info(f"##### Slack message delivered ####")
    except requests.RequestException as e:
        logger.error(f"Error sending message {e}")

load_dotenv()

API_ID=os.environ.get('API_ID')
API_HASH=os.environ.get('API_HASH')
WEBHOOK=os.environ.get('webhook')
channels=['channel_1','channel_2']

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger=logging.getLogger(__name__)

async def main():
    client=TelegramClient('anon',API_ID,API_HASH)

    try:
        await client.start()
        # Fetching all channel entities from channels[]
        channel_entities=await asyncio.gather(*(client.get_entity("channel") for channel in channels))
    except Exception as e:
        logger.error(f"Error fetching channel entities: {e}")

    @client.on(events.NewMessage)
    async def handle_message(event):
        try:
            sender=await event.get_sender()
            channel=await event.get_chat()
            message=event.raw_text

            text=f"Telegram Alert\nChannel: {(channel.title)}\nMessage: {message}\n"
            logger.info(f"Message received from {sender.username} in {channel.title}: {message}")

            await send_message_to_slack(text)
        except Exception as e:
            logger.error(f"Error processing message: {e}")

    # Run client until process is killed
    try:
        await client.run_until_disconnected()
    except Exception as e:
        logger.error(f"Error running the client: {e}")

    return handle_message
asyncio.run(main())



