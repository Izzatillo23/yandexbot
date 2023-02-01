from telebot import TeleBot
from telebot.types import Message, CallbackQuery
from telebot.types import ReplyKeyboardRemove
import time

from config import * 
from keyboard import *
from queris import *
from admin import *

bot = TeleBot(TOKEN)

def admin(message:Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name

    bot.send_message(user_id, f""" Hurmatli 👮‍♂️Adminstarator👮‍♂️ Rasilka Turini Tanlang   """,reply_markup=admin_type())

    



## admin texkst :



@bot.message_handler(func=lambda message:message.text == 'Text📃' and message.from_user.id == ADMIN_ID )

def admin_text(message:Message):

    msg = bot.send_message(ADMIN_ID, f" Fpydalanuvchilarga Yubormoqchi Bolgan Texti Kirting ")
    bot.register_next_step_handler(msg, send_text)



def send_text(message:Message):
    text = message.text
    users = get_all_users()

    for user_id in users:
        bot.send_message(user_id, text)
    
    bot.send_message(ADMIN_ID, f" Hurmatli Adminstrator Habar Barcha Azolarga Yuborildi Faqat Bloc Qilganlardan Tashqari.: ")





## admin img


@bot.message_handler(func=lambda message:message.text == 'Text📃' and message.from_user.id == ADMIN_ID )

def admin_text(message:Message):

    msg = bot.send_message(ADMIN_ID, f" Fpydalanuvchilarga Yubormoqchi Bolgan Texti Kirting ")
    bot.register_next_step_handler(msg, send_text)



def send_text(message:Message):
    text = message.text
    users = get_all_users()

    for user_id in users:
        bot.send_message(user_id, text)
    
    bot.send_message(ADMIN_ID, f" Hurmatli Adminstrator Habar Barcha Azolarga Yuborildi Faqat Bloc Qilganlardan Tashqari.: ")