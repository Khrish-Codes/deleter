from pyrogram import Client, filters

BOT_TOKEN = '6028376714:AAEc-lTbdg0HypAgdXg2Wz3vMeI5WvRjORA'
CHANNEL_ID = -1001604178274  # Replace with your channel ID (a negative integer)

app = Client('my_bot', bot_token=BOT_TOKEN)

@app.on_message(filters.chat(CHANNEL_ID))
def delete_messages(client, message):
    # Delete the incoming message
    message.delete()

if __name__ == "__main__":
    app.run()
