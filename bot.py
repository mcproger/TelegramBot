from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import json
import random
import getpass
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

token = getpass.getpass('Enter your Bot token: ')

def start(bot, update):
    update.message.reply_text('Hi!')

def help(bot, update):
    update.message.reply_text('Help!')

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def news_load():
    filename = 'xpost.json'
    with open(filename, mode="r", encoding='utf-8') as myfile:
        data = json.load(myfile)
    return data

def random_python_news(bot, update):

    post = random.choice(news_load())

    update.message.reply_text(post['attachments'][0]['link']['title'] + post['attachments'][0]['link']['preview_url'])

    return 0


def main():

    updater = Updater(token)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(CommandHandler("python_news", random_python_news))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()