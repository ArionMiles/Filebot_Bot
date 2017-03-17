from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
import logging
import os
import ConfigParser
# Read settings from config file
config = ConfigParser.RawConfigParser()
config.read('bot.ini')
TOKEN = config.get('BOT', 'TOKEN')
APP_NAME = config.get('BOT', 'APP_NAME')
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)

# Setting Webhook
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook(APP_NAME + TOKEN)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

dispatcher = updater.dispatcher

# Real stuff
def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Hi! I'm a telegram Bot for Filebot!")

def intro(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="I'm a telegram Bot for Filebot!")

def chatid(bot, update):
	chatid = str(update.message.chat_id)
	bot.sendMessage(chat_id=update.message.chat_id, text="Your Chat ID is: "+ "*" + chatid + "*", parse_mode='markdown')

def unknown(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't get that.")


# Handlers
start_handler = CommandHandler('start', start)
intro_handler = RegexHandler('Who are you?', intro)
chatid_handler = CommandHandler('chatid', chatid)
unknown_handler = MessageHandler(Filters.command, unknown)
unknown_message = MessageHandler(Filters.text, unknown)

# Dispatchers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(intro_handler)
dispatcher.add_handler(chatid_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(unknown_message)


#dp.add_handler(RegexHandler(r"$What's your name\?^", callback)) FROM jh0ker

updater.start_polling()
updater.idle()