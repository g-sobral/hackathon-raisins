import telegram
from time import sleep

try:
    from urllib.error import URLError
except ImportError:
    from urllib2 import URLError


bot = telegram.Bot('157053965:AAFrYrBkN1upvkzMzJ2y9fBHUaKirhMLvvY')
print 'Bot Telegram iniciado...'

def send_telegram_message(msg):
    bot.sendMessage(chat_id=92329647, text=msg)
