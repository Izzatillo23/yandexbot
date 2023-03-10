from telebot.types import ReplyKeyboardMarkup,KeyboardButton
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup


def generate_registr():
    makrup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_check = KeyboardButton(text='๐ ROYHADAN OTISH ๐')
    makrup.row(btn_check)
    return makrup




def generate_ask_contact_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_ask_contact = KeyboardButton(text="Telefon raqamini jo'natish ๐ฑ", request_contact=True)
    markup.row(btn_ask_contact)
    return markup



def generate_ask_location():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_ask_contact = KeyboardButton(text="lokation jonatish ๐", request_location=True)
    markup.row(btn_ask_contact)
    return markup






def generate_yes_no():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_yes = KeyboardButton(text="Yes โ")
    btn_no = KeyboardButton(text="No โ")
    markup.add(btn_yes, btn_no)
    return markup




def generete_menyu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1 = KeyboardButton(text='๐๐ Mening Malumotlarim ๐ง๐')
    btn2 = KeyboardButton(text='๐Taxi Chaqirish๐ฅ')
    btn3 = KeyboardButton(text='โณ๐Chaqirilgan Taxilar Tarihiโ๐')
    btn4  = KeyboardButton(text="๐จโ๐งIsh Bilan Taminlash๐จ๐๐ธ")
    btn5 = KeyboardButton(text='โ Setings โ')
    markup.add(btn1,btn2,btn3,btn4,btn5)
    return markup




def generate_taxi_sort():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1 = KeyboardButton(text='START ๐')
    btn2 = KeyboardButton(text='STANDART ๐')
    btn3 = KeyboardButton(text='KOMFORT ๐')
    btn4 = KeyboardButton(text='BIZNES ๐')
    markup.add(btn1,btn2,btn3,btn4)
    return markup





def generate_work():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1 = KeyboardButton(text='โญISHKA ROYHADAN OTISH๐ฅ๐ต')
    btn2 = KeyboardButton(text='๐BOSH MENYUโ๐')

    markup.add(btn1,btn2)
    return markup



def generate_job():
    markup = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text='โญISHKA ROYHADAN OTISH๐ฅ๐ต',callback_data='ish')
    btn2 = InlineKeyboardButton(text='๐BOSH MENYUโ๐',callback_data='menyu')
    markup.add(btn1,btn2)
    return markup





def taxi_next():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1 = KeyboardButton(text='โญNEXTโญ')


    markup.add(btn1)
    return markup   









def admin_type():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text='Text๐')
    btn2 = KeyboardButton(text='Img๐ท')
    btn3 = KeyboardButton(text='Video๐ฅ')
    btn4 = KeyboardButton(text='Music๐ต')
    btn5 = KeyboardButton(text='Text๐ + Img๐ท ')
    btn6 = KeyboardButton(text='Text๐ + Video๐ฅ')
    btn7 = KeyboardButton(text='Foydalanauvchilaridi Malumotini korish๐ฅ๐ ')
    
    markup.row(btn1,btn2)
    markup.row(btn3,btn4)
    markup.row(btn5)
    markup.row(btn6)
    markup.row(btn7)

    return markup







