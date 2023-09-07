from telegram.ext import Updater, MessageHandler, Filters

# Replace 'YOUR_BOT_TOKEN' with your bot's token
BOT_TOKEN = '6028376714:AAEc-lTbdg0HypAgdXg2Wz3vMeI5WvRjORA'

def delete_messages(update, context):
    # Delete the incoming message
    update.message.delete()

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Register the message handler to delete all incoming messages
    dp.add_handler(MessageHandler(Filters.all, delete_messages))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
