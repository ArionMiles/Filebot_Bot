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
	#bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
	bot.sendMessage(chat_id=update.message.chat_id, text="Hi! I'm a telegram Bot for Filebot!")

def chatid(bot, update):
	#bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
	chatid = str(update.message.chat_id)
	bot.sendMessage(chat_id=update.message.chat_id, text="Your Chat ID is: "+ "*" + chatid + "*", parse_mode='markdown')

def intro(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="I'm a telegram Bot for Filebot!")

def unknown(bot, update):
	#bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
	bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't get that.")

# Handlers
start_handler = CommandHandler('start', start)
chatid_handler = CommandHandler('chatid', chatid)
intro_handler = MessageHandler('Who are you?', intro)
unknown_command = MessageHandler(Filters.command, unknown)
unknown_message = MessageHandler(Filters.text, unknown)

# Dispatchers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(chatid_handler)
dispatcher.add_handler(intro_handler)
dispatcher.add_handler(unknown_command)
dispatcher.add_handler(unknown_message)

updater.start_polling()
updater.idle()