from pyrogram import Client, filters

BOT_TOKEN = '6028376714:AAEc-lTbdg0HypAgdXg2Wz3vMeI5WvRjORA'
CHANNEL_ID = -1001604178274  # Replace with your channel ID (a negative integer)

# Provide your API ID and API Hash obtained from https://my.telegram.org
API_ID = '23830477'
API_HASH = '19f8365d98fb11c9cd6c1eaa8b1fa4b8'

app = Client('my_bot', bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.chat(CHANNEL_ID))
def delete_messages(client, message):
    # Delete the incoming message
    message.delete()
