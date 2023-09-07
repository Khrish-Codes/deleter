from pyrogram import Client, filters

# Replace 'API_ID' and 'API_HASH' with your own values.
API_ID = '23830477'
API_HASH = '19f8365d98fb11c9cd6c1eaa8b1fa4b8'
BOT_TOKEN = '6028376714:AAEc-lTbdg0HypAgdXg2Wz3vMeI5WvRjORA'
CHANNEL_NAME = 'MOVIES HUB ALPHA UPLOADING'

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(CHANNEL_NAME))
def delete_messages(client, message):
    # Delete the incoming message
    message.delete()

if __name__ == "__main__":
    app.run()
