from telebot import TeleBot
from telebot.types import Message
from time import sleep
from bob_telegram_tools.utils import TelegramTqdm
from bob_telegram_tools.bot import TelegramBot

from config import *


bot = TeleBot(token=TOKEN)



@bot.message_handler(commands=['start'])
def command_start(message: Message):
    print(message.message_id, 'id')
    percent = 0
    user_id = message.from_user.id
    chat_id = message.chat.id

    bot = TelegramBot(TOKEN, user_id)

    pb = TelegramTqdm(bot)
    
    for i in pb(range(10)):
        sleep(1)
        print(i)
        print(pb)
        
    
    dos(message)






def dos(message:Message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    bot.send_message(user_id, 'text')



bot.polling(none_stop=True)







































