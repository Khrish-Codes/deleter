import logging
from pyrogram import Client, filters

# Replace 'API_ID' and 'API_HASH' with your own values.
API_ID = '23830477'
API_HASH = '19f8365d98fb11c9cd6c1eaa8b1fa4b8'
BOT_TOKEN = '6028376714:AAEc-lTbdg0HypAgdXg2Wz3vMeI5WvRjORA'
CHANNEL_NAME = 'MOVIES HUB ALPHA UPLOADING'
OWNER_USER_ID = '6408116706'  # Replace with the owner's user ID

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename='bot.log',  # Specify the log file name
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(CHANNEL_NAME))
def delete_messages(client, message):
    # Get the username of the sender (optional)
    sender_username = message.from_user.username if message.from_user else "Unknown User"
    
    # Delete the incoming message
    message.delete()
    
    # Send a notification to the owner's DMs
    owner_message = f"Deleted message in {CHANNEL_NAME}:\n\nFrom: @{sender_username}\n\n{message.text}"
    client.send_message(OWNER_USER_ID, owner_message)
    
    # Log the deleted message
    logger.info(f"Deleted message in {CHANNEL_NAME}:\nFrom: @{sender_username}\n{message.text}")

if __name__ == "__main__":
    app.run()
