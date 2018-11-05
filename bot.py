from telegram.ext import Updater
from src.paser import get_new
import datetime
import logging

logger = logging.getLogger('cian_bot')
logger.setLevel(logging.DEBUG)

url = 'https://www.cian.ru/cat.php?deal_type=rent&engine_version=2&metro[0]=85&offer_type=flat&region=1&room2=1&type=4'
save_file = 'save.json'
token = 'Token here'


def update(bot, job):
    flats = get_new(url, save_file)
    user_ids = ['User ids here']
    if flats:
        text = str(flats)
        for id in user_ids:
            bot.send_message(chat_id=id, text=text)
    else:
        for id in user_ids:
            bot.send_message(chat_id=id, text='Nothing new, sorry.')


if __name__ == '__main__':
    updater = Updater(token)
    job = updater.job_queue
    job.run_repeating(update, datetime.timedelta(minutes=30), 10)
    updater.start_polling()
    updater.idle()
