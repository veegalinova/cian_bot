from telegram.ext import Updater
from paser import get_flats
import datetime
import logging

logger = logging.getLogger('cian_bot')
logger.setLevel(logging.DEBUG)

url = 'https://www.cian.ru/cat.php?currency=2&deal_type=rent&engine_version=2' \
      '&foot_min=15&maxprice=46000&metro%5B0%5D=77&metro%5B1%5D=85&metro%5B2%5D=129' \
      '&offer_type=flat&only_foot=2&room1=1&room2=1&type=4'
save_file = 'save.json'
token = 'Token here'


def update(bot, job):
    flats = get_flats(url, save_file)
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
