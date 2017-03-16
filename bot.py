from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
import ConfigParser
# Read settings from config file
config = ConfigParser.RawConfigParser()
config.read('bot.ini')
TOKEN = config.get('BOT', 'TOKEN')
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)

# Setting Webhook
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook("https://filebot-backend.herokuapp.com/" + TOKEN)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

dispatcher = updater.dispatcher

# Real stuff
def start(bot, update):
	 bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
	bot.sendMessage(chat_id=update.message.chat_id, text="Hi!")

def chatid(bot, update):
	 bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
	chatid = str(update.message.chat_id)
	bot.sendMessage(chat_id=update.message.chat_id, text=chatid)

def unknown(bot, update):
	 bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
	bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't get that.")

# Handlers
start_handler = CommandHandler('start', start)
chatid_handler = CommandHandler('chatid', chatid)
unkown_handler = MessageHandler(Filters.command, unknown)

# Dispatchers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(chatid_handler)
dispatcher.add_handler(unkown_handler)

updater.start_polling()
updater.idle()