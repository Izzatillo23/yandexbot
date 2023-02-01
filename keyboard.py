from telebot.types import ReplyKeyboardMarkup,KeyboardButton
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup


def generate_registr():
    makrup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_check = KeyboardButton(text='📋 ROYHADAN OTISH 📋')
    makrup.row(btn_check)
    return makrup




def generate_ask_contact_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_ask_contact = KeyboardButton(text="Telefon raqamini jo'natish 📱", request_contact=True)
    markup.row(btn_ask_contact)
    return markup



def generate_ask_location():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_ask_contact = KeyboardButton(text="lokation jonatish 📍", request_location=True)
    markup.row(btn_ask_contact)
    return markup






def generate_yes_no():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_yes = KeyboardButton(text="Yes ✅")
    btn_no = KeyboardButton(text="No ❌")
    markup.add(btn_yes, btn_no)
    return markup




def generete_menyu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1 = KeyboardButton(text='🔐📑 Mening Malumotlarim 🧑📂')
    btn2 = KeyboardButton(text='📞Taxi Chaqirish📥')
    btn3 = KeyboardButton(text='⏳📊Chaqirilgan Taxilar Tarihi⌛📊')
    btn4  = KeyboardButton(text="👨‍🔧Ish Bilan Taminlash👨🔊💸")
    btn5 = KeyboardButton(text='⚙ Setings ⚙')
    markup.add(btn1,btn2,btn3,btn4,btn5)
    return markup




def generate_taxi_sort():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1 = KeyboardButton(text='START 🚗')
    btn2 = KeyboardButton(text='STANDART 🚕')
    btn3 = KeyboardButton(text='KOMFORT 🚖')
    btn4 = KeyboardButton(text='BIZNES 🚘')
    markup.add(btn1,btn2,btn3,btn4)
    return markup





def generate_work():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1 = KeyboardButton(text='⭕ISHKA ROYHADAN OTISH📥💵')
    btn2 = KeyboardButton(text='📄BOSH MENYU✔😉')

    markup.add(btn1,btn2)
    return markup



def generate_job():
    markup = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text='⭕ISHKA ROYHADAN OTISH📥💵',callback_data='ish')
    btn2 = InlineKeyboardButton(text='📄BOSH MENYU✔😉',callback_data='menyu')
    markup.add(btn1,btn2)
    return markup





def taxi_next():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1 = KeyboardButton(text='⏭NEXT⏭')


    markup.add(btn1)
    return markup   









def admin_type():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text='Text📃')
    btn2 = KeyboardButton(text='Img📷')
    btn3 = KeyboardButton(text='Video🎥')
    btn4 = KeyboardButton(text='Music🎵')
    btn5 = KeyboardButton(text='Text📃 + Img📷 ')
    btn6 = KeyboardButton(text='Text📃 + Video🎥')
    btn7 = KeyboardButton(text='Foydalanauvchilaridi Malumotini korish👥🛄 ')
    
    markup.row(btn1,btn2)
    markup.row(btn3,btn4)
    markup.row(btn5)
    markup.row(btn6)
    markup.row(btn7)

    return markup







