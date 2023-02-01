from telebot import TeleBot
from telebot.types import Message, CallbackQuery
from telebot.types import ReplyKeyboardRemove
import time
from random import randint
import time
import replit
import datetime

from bob_telegram_tools.utils import TelegramTqdm
from bob_telegram_tools.bot import TelegramBot
from time import sleep

from config import * 
from keyboard import *
from queris import *
from admin import *
from orasidagimasofa import distnca_city

##--------------------------------------------------------------------------------------------------------
## geopoy shaxarlar orasidagi masofani chiqarish uchun hamda lokatsiya malumotlarni olgan kerak

from geopy import Nominatim  
nomainaltim = Nominatim(user_agent='user',timeout=None)

##--------------------------------------------------------------------------------------------------------

bot = TeleBot(TOKEN,parse_mode='html')


##--------------------------------------------------------------------------------------------------------
## menyu lardi boshqarish va qoshish 

@bot.message_handler(commands=['start','menyu','chanel','deweloper'])



##--------------------------------------------------------------------------------------------------------
##  foydalanuvchini royhadan otkan otmaganligini sorash

def command_start (message:Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name

    print(user_id)

    if message.text == '/start':


        users = get_all_users()
        if user_id == ADMIN_ID :
            bot.send_message(user_id, f" adminstrator")
            user_id = message.from_user.id

            admin(message)
           
            # bot.send_message(user_id, f""" Asalomu alaykum hurmatli {user_name} bot 
            #                 foydalanuvchisi  siz royhatan o'tkan ekansiz😉 ..  """,reply_markup=ReplyKeyboardRemove())
            # tekshirish(message)

        elif user_id in users:
            user_name = message.from_user.full_name
            bot.send_message(user_id, f" Asalomu Alaykum Hurmatli {user_name} Foydalanuvchi siz royhadan otkana ekansiz SHaxsiy parolingizni kirting . ",reply_markup=ReplyKeyboardRemove())
            bot.send_message(user_id,f""" hozirgi vaqt >> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} """)
            tekshirish(message)
        
        
        else:
            bot.send_message(user_id, f""" Asalomu Alaykum hurmatli {user_name}  
                            foydalanuvchi bot dan toliq foydalanish uchun royhatan otshingiz zarur !!✔✔🛑🛑🛑 ..  """,reply_markup=generate_registr())


            


        



##--------------------------------------------------------------------------------------------------------


####  bu yerga cammanda buyruq qoshsa boladi 


    elif message.text == '/menyu':
        menyu(message)
    

    elif message.text == '/chanel':
        chanel_post(message)

    elif message.text == '/deweloper':
        deweloper(message)


##--------------------------------------------------------------------------------------------------------    





def deweloper(message:Message):
    user_id = message.from_user.id

    bot.send_message(user_id,f" DEWELOPER >>  G'ULOMOV IZZATILLO 😎⏭⏭   https://t.me/izzatillo022   ")

    menyu(message)








##--------------------------------------------------------------------------------------------------------

##  ADMIN PANEL ADMINSTARATOR UCHUN

##--------------------------------------------------------------------------------------------------------



    





def admin(message:Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name

    bot.send_message(user_id, f""" Hurmatli 👮‍♂️Adminstarator👮‍♂️ Rasilka Turini Tanlang   """,reply_markup=admin_type())

    



## admin texkst :



@bot.message_handler(func=lambda message:message.text == 'Text📃' and message.from_user.id == ADMIN_ID )

def admin_text(message:Message):

    msg = bot.send_message(ADMIN_ID, f" Foydalanuvchilarga Yubormoqchi Bolgan Texti Kirting ")
    bot.register_next_step_handler(msg, send_text)



def send_text(message:Message):
    text = message.text
    users = get_all_users()

    for user_id in users:
## boti bloc qilinganda ishlatiladi 
        try :
            bot.send_message(user_id, text)
        
        except Exception:
            continue
    
    bot.send_message(ADMIN_ID, f" Hurmatli Adminstrator Habar Barcha Azolarga Yuborildi Faqat Bloc Qilganlardan Tashqari.: ")









# ## admin img


@bot.message_handler(func=lambda message:message.text == 'Img📷' and message.from_user.id == ADMIN_ID )

def admin_text(message:Message):

    msg = bot.send_message(ADMIN_ID, f" Foydalanuvchilarga Yubormoqchi Bolgan img Kirting ")
    bot.register_next_step_handler(msg, send_img)



def send_img(message:Message):
    ## rasimga fayil id olish
    image = message.photo[-1].file_id
    users = get_all_users()

    if  message.content_type == 'photo':
        for user_id in users:
## boti bloc qilinganda ishlatiladi 
            try :
                bot.send_photo(user_id, image)
        
            except Exception:
                continue
                 
        bot.send_message(ADMIN_ID, f" Hurmatli Adminstrator Habar Barcha Azolarga Yuborildi Faqat Bloc Qilganlardan Tashqari.: ")



    else:
        bot.send_message(ADMIN_ID, f" siz tekst kirtingiz !! rasim kirting  ")






#>>>>>>>>>>>>>>>>>> video 



@bot.message_handler(func=lambda message:message.text == 'Video🎥' and message.from_user.id == ADMIN_ID )

def admin_video(message:Message):

    msg = bot.send_message(ADMIN_ID,' ADMINSTRATOR  FOYDALANUVCHILARGA YUBOR MOQCHI BOLGAN VIDEONI KIRTING   ',reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, send_vidoe)



def send_vidoe(message:Message):

    if  message.content_type == 'video':
        video = message.video.file_id
        users = get_all_users()
        for user_id in users:
## boti bloc qilinganda ishlatiladi 
            try :
                bot.send_vidoe(user_id, video)
        
            except Exception:
                continue
                 
        bot.send_message(ADMIN_ID, f" Hurmatli Adminstrator Habar Barcha Azolarga Yuborildi Faqat Bloc Qilganlardan Tashqari.: ")
        admin(message)


    else:
        bot.send_message(ADMIN_ID, f" siz tekst kirtingiz !! vidoe kirting  ")
        admin(message)





@bot.message_handler(func=lambda message:message.text == 'Foydalanauvchilaridi Malumotini korish👥🛄' and message.from_user.id == ADMIN_ID )



def send_users(message:Message):

    usee = get_all_users_chanel()
    for i in usee:
#izzatillo ALHAMDULLILAH
      bot.send_message(ADMIN_ID, f""" BO'T FOYDALANUVCHISI >>  
      _id♻   ✅ =  {i[0]}
      NAME    🔲 =  {i[1]}
      NUMBER  🔲 =  {i[2]}
      PASWORD ⬛ =  {i[3]}""",reply_markup=ReplyKeyboardRemove())

    bot.send_message(ADMIN_ID,f" barcha foydalanuvchilar malumoti yuborlidi : .. ")
    
    admin(message)

    




# @bot.message_handler(func=lambda message:message.text == 'Text📃 + Img📷 ' and message.from_user.user_id == ADMIN_ID )
# @bot.message_handler(func=lambda message:message.text == 'Text📃 + Video🎥' and message.from_user.user_id == ADMIN_ID )



##--------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------




### loading uchun 


def command_loading(message: Message):
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





##--------------------------------------------------------------------------------------------------------
## >>  /chanel kammandasini yozsa faqat
## kanalga malumot yuborish

def chanel_post(message:Message):
    usee = get_all_users_chanel()
    for i in usee:
#izzatillo ALHAMDULLILAH
      bot.send_message(CHANEL_ID, f""" BO'T FOYDALANUVCHISI >>  
      _id♻   ✅ =  {i[0]}
      NAME    🔲 =  {i[1]}
      NUMBER  🔲 =  {i[2]}
      PASWORD ⬛ =  {i[3]}""")

    menyu(message)


##--------------------------------------------------------------------------------------------------------









##--------------------------------------------------------------------------------------------------------


### paroldi sorash 


def tekshirish(message:Message):
    user_id = message.from_user.id
    user_name = message.from_user.username

    msg = bot.send_message(user_id, f""" Asalomu Alaykum hurmatli {user_name}  
                        Foydalanuvchi  shaxsiy parolingizni kirting .🔒🔏🛅🗝🔑.  """)
    bot.register_next_step_handler(msg, command_tekshirish)
    




## loading  loading loading


def command_tekshirish(message: Message):

    percent = 0
    user_id = message.from_user.id
    chat_id = message.chat.id
    
    bot = TelegramBot(TOKEN, user_id)
    
    pb = TelegramTqdm(bot,'loading..')
    
    
    for i in pb(range(2)):
        sleep(1)


    
    pasword_chack(message)






##--------------------------------------------------------------------------------------------------------

### foydalanuvchi royhadan otkan bolsa parolini sorab botka kirgazish




def pasword_chack(message:Message):
    user_id = message.from_user.id
    user_name = message.from_user.username

    pasword_reg = message.text
    pasword = get_pasword(user_id,pasword_reg)
    print(pasword)

    if pasword:
        bot.send_message(user_id, f"   {user_name} Parol Tasdiqlandi  💯✅ ")
        bot.send_photo(user_id, photo= open( 'delivery_taxi_13.jpg','rb'))
        menyu(message)

        
    
    else:

        bot.send_message(user_id, f" {user_name} Hurmatli  Foydalanuvchi Kiritkan Parolingiz Notogri ❗🚫❌ ")
        tekshirish(message)


##--------------------------------------------------------------------------------------------------------




##--------------------------------------------------------------------------------------------------------

###  royhadan otish


users_data = {}  ## bunga foydalanuvchi malumotlarini logat kornishda saqlab turib vaqtinchalik keyin malumotlar omboriga yozish


@bot.message_handler(func=lambda message: message.text == "📋 ROYHADAN OTISH 📋")
def ask_full_name(message: Message):
    global users_data
    user_id = message.from_user.id
    users_data[user_id] = {
        'user_id': user_id
    }
    print(users_data)
    msg = bot.send_message(user_id, "To'liq ism familyangizni kirting:🟩🆑 ",
                           reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, ask_contact)






def ask_contact(message: Message):
    global users_data
    user_id = message.from_user.id
    full_name = message.text
    users_data[user_id].update({'full_name': full_name})
    print(users_data)
    msg = bot.send_message(user_id, "Telefon raqamingizni Yuboring📞☎: ",
                           reply_markup=generate_ask_contact_button())
    bot.register_next_step_handler(msg, ask_lokation)






def ask_lokation(message: Message):
    global users_data
    user_id = message.from_user.id
    if message.content_type == 'contact':
        contact = message.contact.phone_number
        users_data[user_id].update({'contact': contact})
        print(users_data)
    elif message.content_type == 'text':
        contact = message.text
        users_data[user_id].update({'contact': contact})
        print(users_data)

    msg = bot.send_message(user_id, "Lokatsiyangizni Yuboring:📍 ",
                           reply_markup=generate_ask_location())
    bot.register_next_step_handler(msg, user_pasword)





##--------------------------------------------------------------------------------------------------------
## >> foydalanuvchi   pasword qoyish 



def user_pasword(message:Message):
    global users_data
    user_id = message.from_user.id
    user_name = message.from_user.username
    lat = message.location.latitude
    lon = message.location.longitude

    cordinats = (lat,lon)
    lokiation = nomainaltim.reverse(cordinats)
    print(lokiation)
    users_data[user_id].update({'lokation': lokiation})

    msg = bot.send_message(user_id, f" {user_name} SHaxsiy Parol 🛅 Kirting 4-harif🔠 yoki sondan🔢 iborat bo'lsin   ",reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, show_data)






##--------------------------------------------------------------------------------------------------------

## ragistiratsiya malumotlarini korsatish   

def show_data(message:Message):
    global users_data
    user_id = message.from_user.id
    user_name = message.from_user.full_name 

    pasword = message.text
    users_data[user_id].update({'pasword':pasword})


   
    bot.send_message(user_id, f""" {user_name} Kiritgan Malumotlaringiz Togrimi ➡➡   """)

    msg = bot.send_message(user_id, f""" hozirgi vaqt >> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}
                              ism familya > {users_data[user_id]['full_name']} 
                              telfon raqam  > {users_data[user_id]['contact']}
                              lokation      > {users_data[user_id]['lokation']}
                              pasword       > {users_data[user_id]['pasword']}
                               
    """,reply_markup=generate_yes_no())

    bot.register_next_step_handler(msg, command_registr)

    






def command_registr(message: Message):

    percent = 0
    user_id = message.from_user.id
    chat_id = message.chat.id

    bot = TelegramBot(TOKEN, user_id)

    pb = TelegramTqdm(bot,'12load')
    
    for i in pb(range(6)):
        sleep(1)

    
    show_congurlation(message)

##--------------------------------------------------------------------------------------------------------



## registratsiya malumotlarini sorab agar ha ni bosa database ga maluotlardi yozish

def show_congurlation(message:Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    if message.text == 'Yes ✅':

        insert_user(telegram_id=users_data[user_id]['user_id'],
                    full_name=users_data[user_id]['full_name'],
                    contact=users_data[user_id]['contact'],
                    pasword=users_data[user_id]['pasword']),
                    
        users_data.pop(user_id)

        bot.send_message(user_id, f" {user_name} TABRIKLAYMIZ SIZ ROYHADAN MUVAFAQIYATLI OTINGIZ  🎆🎇🎉🎉🎉🎉 ")
        menyu(message)
    elif message.text == 'No ❌':
        bot.send_message(user_id, f"  Registratsiyadan O'tishda Etiborli Boling ⚙ .. ")
        ask_full_name(message)






##--------------------------------------------------------------------------------------------------------


## >>>   kodi kiritkandan keyin menyu ekranini  ..... chiqarish




def menyu(message:Message):
    if message.text == '/start':
        command_start(message)
    
    elif message.text == '/deweloper':
        deweloper(message)
    


    

    else:
        user_id = message.from_user.id
        user_name = message.from_user.username
    
        bot.send_message(user_id, f"  {user_name}  Kerakli Bolimdi Tanleng🎛♻  ",reply_markup=generete_menyu())


##--------------------------------------------------------------------------------------------------------


## settings uchun 

@bot.message_handler(func=lambda message: message.text == "⚙ Setings ⚙")

def settings(message:Message):
    user_id = message.from_user.id
    user_name = message.from_user.username

    bot.send_message( user_id , f"  Hurmatli {user_name} Hozirda Bu Bo'lim bo'sh 😉 " )












##--------------------------------------------------------------------------------------------------------
## meninig malumotlarim foydalanuvchi malumotlari



@bot.message_handler(func=lambda message: message.text == "🔐📑 Mening Malumotlarim 🧑📂")
def standart_taxi(message:Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_data = get_user_shaxsiy(user_id)
    for i in user_data:

     bot.send_message(user_id, f""" your id {i[0]}
     your full_name    🆑   {i[1]} 
     your phone number 🅱   {i[2]}
     your pasword      🛑   {i[3]} """)


##--------------------------------------------------------------------------------------------------------






##--------------------------------------------------------------------------------------------------------

###  inline keyboard bilan ishlash


## ish bilan taminlash  komandasi

yandex_job = {}


@bot.message_handler(func=lambda message: message.text == "👨‍🔧Ish Bilan Taminlash👨🔊💸")



def taxi_select(message:Message):
    global yandex_job

    user_id = message.from_user.id
    chat_id = message.chat.id
    user_name = message.from_user.username
    

    yandex_job[chat_id] = {
        'chat_id':chat_id
    }
    print(yandex_job)
    bot.send_message(chat_id, '..',reply_markup=ReplyKeyboardRemove())
    bot.send_message(chat_id,f""" Asalomu Alaykum {user_name} sizda Avtomobil🚗 Bormi ✔✅ 
    Unda Ushbu imkonyatlardan ⏭ Foydalaning bizning bo'tan ro'yhadan oting Hamda biz bilan Birgalikda 
    Yuksaling😉⚡ """,reply_markup=generate_job())









@bot.callback_query_handler(func=lambda call: call.data in ['ish','menyu'])

def user_job(call: CallbackQuery):
    chat_id = call.message.chat.id
    data = call.data
    print(data)

    if data == 'ish':

        chat_id = call.message.chat.id
        msg = bot.send_message(chat_id,f""" Toliq ism familyangizni Kirting ✍ """,reply_markup=ReplyKeyboardRemove())
    
        bot.delete_message(chat_id, call.message.message_id)
    
        bot.register_next_step_handler(msg,name_job)
    
    else:
        bot.send_message(chat_id,f" BOSH MENYU 🏠 ",reply_markup=generete_menyu())
        bot.delete_message(chat_id, call.message.message_id)






def name_job(message:Message):

    chat_id = message.chat.id
    job_name = message.text
    msg = bot.send_message(chat_id, f" Telfon raqamingizni Yuboring 📲 ",reply_markup=generate_ask_contact_button())
    yandex_job[chat_id].update({'job_name': job_name})
    print(yandex_job)

    bot.register_next_step_handler(msg,contact_job)








def contact_job(message:Message):
    chat_id = message.chat.id
    
    if message.content_type == 'contact':
        job_contact = message.contact.phone_number
        yandex_job[chat_id].update({'job_contact':job_contact})

    elif message.content_type == 'text':
        job_contact = message.text
        yandex_job[chat_id].update({'job_contact':job_contact})
    
    msg = bot.send_message(chat_id, f" Moshinagiz Rusumi 🏎🚗 : ",reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg,moshina_job)



def moshina_job(message:Message):
    chat_id = message.chat.id

    if message.content_type == 'text':
        job_avto = message.text
    
        yandex_job[chat_id].update({'job_avto':job_avto})
        print(yandex_job)
        msg = bot.send_message(chat_id, f" 👉Hurmatli foydalanuvchi sizning arizangiz qabul qilindi operatorlarimiz ozlari siz bilan bog'lanishadi📶📴  :  ")
        chanel_sent(message)
    else:
        bot.send_message(chat_id, f" Hurmatli Foydalanuvchi Text Ko'rnishida Kirting Raqam emas !! ")
        contact_job(message)
    



def chanel_sent(message:Message):
    chat_id = message.chat.id
    

         
    bot.send_message(CHANEL_JOB,f""" ariza qoldirilgan vaqt :>> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}
     SHopir haqida malumot Chat_id {yandex_job[chat_id]['chat_id']}
    shoopir_name  {yandex_job[chat_id]['job_name']}
    shopir_contackt {yandex_job[chat_id]['job_contact']}
    shopir_avto {yandex_job[chat_id]['job_avto']}
        """ )
    menyu(message)




## contact = {users_taxi_histiry[user_id]['user_contact']} 







# @bot.callback_query_handler(func=lambda call: call.data in ['menyu'])

# def user_job_menyu(call: CallbackQuery):

#     chat_id = call.message.chat.id
#     msg = bot.send_message(chat_id,f" BOSH MENYU ")
#     menyu(message) 









##--------------------------------------------------------------------------------------------------------









###  taxi chaqirish uchun >>





@bot.message_handler(func=lambda message: message.text == "📞Taxi Chaqirish📥")



def taxi_select(message:Message):
    chat_id = message.chat.id

    user_id = message.from_user.id
    user_name = message.from_user.username

    percent = 0
    user_id = message.from_user.id
    for i in range(1):
      replit.clear()
      percent +=1
      s =  time.sleep(randint(1,1))


      print(percent)

    
      bot.send_message(user_id, f"  loading % {percent}   ")

      bot.send_video(user_id, video=open('lok2_Trim_Trim3_Trim444.mp4','rb'),caption="lokatsiya yuborish buyicha qo'lanma📍✔")



    bot.send_message(user_id, f" Hurmatli {user_name} hamyoningizga mos 🚘avtomobil🚗 turini tanlang✔🟩: .. ",reply_markup=generate_taxi_sort())











##--------------------------------------------------------------------------------------------------------


##  foydalanuvchi chaqirgan taxilar royhatini choqarib beradi


@bot.message_handler(func=lambda message: message.text == "⏳📊Chaqirilgan Taxilar Tarihi⌛📊")




## loading  loading loading

def command_chaqirilgan(message: Message):

    percent = 0
    user_id = message.from_user.id
    chat_id = message.chat.id
    
    bot = TelegramBot(TOKEN, user_id)
    
    pb = TelegramTqdm(bot,'loading..')
    
    
    for i in pb(range(2)):
        sleep(1)

    taxi_histiry(message)






def taxi_histiry(message:Message):
    user_id = message.from_user.id
    user_name = message.from_user.username

    user_taxi_histry = select_historiy(user_id)

    for i in user_taxi_histry:
      time.sleep(2)

      bot.send_message(user_id, f""" hurmatli telfon raqam >> {i[0]} 
      taxi sort  ♻🚘  {i[1]}
      price 💲💵 {i[2]}
      adress  1️⃣📍 {i[3]}
      adress 2️⃣📍 {i[4]}  
      masofa ♻ {i[5]}""")







##--------------------------------------------------------------------------------------------------------

users_taxi_histiry = {}

@bot.message_handler(func=lambda message: message.text == "START 🚗")

def start_taxi(message:Message):
    global users_taxi_histiry
    user_id = message.from_user.id
    user_name = message.from_user.username
    users_taxi_histiry[user_id] = {
        'user_id': user_id
    }
    print(users_taxi_histiry)
    one_lokation(message)


    
##--------------------------------------------------------------------------------------------------------

## zahira uchun ishlagani yoq
users_taxi_standart = {}

@bot.message_handler(func=lambda message: message.text == "STANDART 🚕")

def standart_taxi(message:Message):
    global users_taxi_histiry
    user_id = message.from_user.id
    user_name = message.from_user.username
    users_taxi_histiry[user_id] = {
        'user_id': user_id
    }
    print(users_taxi_histiry)
    one_lokation_standart(message)
    

##--------------------------------------------------------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == "KOMFORT 🚖")
def komfort_taxi(message:Message):
    global users_taxi_histiry
    user_id = message.from_user.id
    user_name = message.from_user.username
    users_taxi_histiry[user_id] = {
        'user_id': user_id
    }
    print(users_taxi_histiry)
    one_lokation_komfort(message)


##--------------------------------------------------------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == "BIZNES 🚘")
def binznes_taxi(message:Message):
   global users_taxi_histiry
   user_id = message.from_user.id
   user_name = message.from_user.username
   users_taxi_histiry[user_id] = {
       'user_id': user_id
   }
   print(users_taxi_histiry)
   one_lokation_biznes(message)



##--------------------------------------------------------------------------------------------------------




def one_lokation(message:Message):
    global users_taxi_histiry
    user_id = message.from_user.id
    user_name = message.from_user.username


    sort_taxi = message.text
    users_taxi_histiry[user_id].update({
        'taxi_sort': sort_taxi
    })
    msg = bot.send_message(user_id, f" HURMATLI FOYDALANUVCHI LOKATSIYANGIZNI  YUBORING 📤 ",reply_markup=generate_ask_location())
    print(users_taxi_histiry)
    bot.register_next_step_handler(msg, next_two_lokation)





def next_two_lokation(message:Message):
    global users_taxi_histiry
    user_id = message.from_user.id


    if message.content_type == 'location':


        user_id = message.from_user.id
        lat = message.location.latitude
        lon = message.location.longitude


        cordinats = (lat,lon)
        lokiation = nomainaltim.reverse(cordinats)
        print(lokiation)
        lokation_str1 = str(lokiation)

        


        msg = bot.send_message(user_id, f"  HURMATLI FOYDALANUVCHI BORMOQCHI 🚶‍♂️ ⏭ BOLGAN MANZILINGIZNI LOKATSIYASINI YUBORING 📤",reply_markup=generate_ask_location())
        users_taxi_histiry[user_id].update({
            'user_one_lokation': lokation_str1
        })
        print(users_taxi_histiry)
        bot.register_next_step_handler(msg, show_lokation,lokiation,cordinats)
    
    elif message.text == '/menyu':
        menyu(message)
    

    else:
        bot.send_message(user_id, f" iltimos lokation yuboring ")
        one_lokation(message)



    #lokatsiyani qayatarib jonatish
    # bot.send_location(user_id, lat, lon)




### ikkita loklatsiyani chiqarisah srat_taxi 




def show_lokation(message:Message,lokiation,cordinats):
    global users_taxi_histiry
    user_id = message.from_user.id
    user_name = message.from_user.full_name

 

    lat = message.location.latitude
    lon = message.location.longitude
    cordinats2 = (lat,lon)
    print(cordinats2)
    lokiation2 = nomainaltim.reverse(cordinats2)
    
    lokation_str2 = str(lokiation2)
    
    
    # bot.send_message(user_id, f" kordinata {cordinats2} ")
    msg = bot.send_message(user_id, f" Telfon Raqamingizni Kirting 📳 : ",reply_markup= generate_ask_contact_button())
    users_taxi_histiry[user_id].update({
        'user_two_lokation': lokation_str2
    })
    print(users_taxi_histiry)
    bot.register_next_step_handler(msg, taxe_call_me,cordinats2,cordinats,lokiation,lokiation2)





##--------------------------------------------------------------------------------------------------------

#### taxi chaqirish uchun yozilgan maulomotlar



def taxe_call_me(message:Message,cordinats2,cordinats,lokiation,lokiation2):
    global users_taxi_histiry
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    if message.content_type == 'contact':
        user_contact = message.contact.phone_number
        users_taxi_histiry[user_id].update({
            'user_contact': user_contact
        })
        print(users_taxi_histiry)
    elif message.content_type == 'text':
        user_contact = message.text
        users_taxi_histiry[user_id].update({
            'user_contact': user_contact
        })

    time.sleep(2)
    msg = bot.send_message(user_id, f" {user_name} ⏭⏭⏭ : > ",reply_markup=taxi_next())
    bot.register_next_step_handler(msg,sitiy_distance,cordinats2,cordinats,lokiation,lokiation2)




    

    
##--------------------------------------------------------------------------------------------------------





## orasidagi masofa hamda borishdagi narhini chiqazib beradi 

def sitiy_distance(message:Message,cordinats,cordinats2,lokiation,lokiation2):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    global users_taxi_histiry
    
    print(cordinats)
    print(cordinats2)

    
    distancee = distnca_city(cordinats, cordinats2)
    print(distancee)
    pe = int(distancee)
    taxi_str = pe * 3.600
    taxi_price = str(taxi_str)

    
    users_taxi_histiry[user_id].update({
        'shaxarlar_oarasidagi_masofa': pe
    })
    print(users_taxi_histiry)


    bot.send_message(user_id, f""" this Time ⌚ ⏭ {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}
     {user_name} SHaxarlar Orasidagi Masofa ⏭ : {pe}.km  Taxminiy yetib  borish narxi 
    👉 {pe*3.600} Ming So'm 💵💲""")

    users_taxi_histiry[user_id].update({
        'taxi_price': taxi_price
    })
    print(users_taxi_histiry)

    msg = bot.send_message(user_id, f" {user_name} TAXI CHAQIRILSINMI 🚖✅ ",reply_markup = generate_yes_no())

    bot.register_next_step_handler(msg, show_send_chanel)
    



        







##--------------------------------------------------------------------------------------------------------


## kanalga zakaz yuborish 


def show_send_chanel(message:Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name 

    no = message.text 

    if message.text == 'Yes ✅':

        msg = bot.send_message(CHANEL_ZAKAZ, f""" taxi chaqirilgan vaqit ⌚ ⏭ {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}
            contact = {users_taxi_histiry[user_id]['user_contact']} ,
            taxi_sort= {users_taxi_histiry[user_id]['taxi_sort']}, 
            price= {users_taxi_histiry[user_id]['taxi_price']}
            adress_lokation= {users_taxi_histiry[user_id]['user_one_lokation']}
            adress_lokation2= {users_taxi_histiry[user_id]['user_two_lokation']}
           sitiy_distance= {users_taxi_histiry[user_id]['shaxarlar_oarasidagi_masofa']}
        """)
        time.sleep(3)
        command_laoding_chanel(message)

    elif message.text == 'No ❌':
        bot.send_message(user_id, f" {user_name}  SIZ NING SOROVINGIZ BEKOR QILINDI ⭕❌ " )
        menyu(message)




##--------------------------------------------------------------------------------------------------------


def command_laoding_chanel(message: Message):

    percent = 0
    user_id = message.from_user.id
    chat_id = message.chat.id

    bot = TelegramBot(TOKEN, user_id)

    pb = TelegramTqdm(bot,'loading..')
    
    for i in pb(range(10)):
        sleep(1)

    
    show_taxi(message)








##--------------------------------------------------------------------------------------------------------

### foydalanuvchiga kirtilgan malumotlarini tog'rligini soredi


def show_taxi(message:Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name 

    msg = bot.send_message(user_id, f""" this Time ⌚ ⏭ {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}
        contact☎ = {users_taxi_histiry[user_id]['user_contact']} ,
        taxi_sort🚖 = {users_taxi_histiry[user_id]['taxi_sort']}, 
        price= {users_taxi_histiry[user_id]['taxi_price']}
        Qayerdan 📌 = {users_taxi_histiry[user_id]['user_one_lokation']}
        Qayerga 📍 = {users_taxi_histiry[user_id]['user_two_lokation']}
       Shaxarlar prasidagi masofa🎛 = {users_taxi_histiry[user_id]['shaxarlar_oarasidagi_masofa']}
    .km""",reply_markup=generate_yes_no())
    bot.send_message(user_id, f" {user_name} taxi chaqirildi  ")
    bot.send_message(user_id, f" {user_name} MALUMOTLAR SAQLANSINMI YES/NO KEYINCHALIK CHAQIRGAN TAXI LARIZ TARIXINI KO'RISH IMKONINI BERADI🔲♻ ")



    bot.register_next_step_handler(msg, command_saqlash)










## loading  loading loading  saqalsh


def command_saqlash(message: Message):

    percent = 0
    user_id = message.from_user.id
    chat_id = message.chat.id
    
    bot = TelegramBot(TOKEN, user_id)
    
    pb = TelegramTqdm(bot,'loading..')
    
    
    for i in pb(range(2)):
        sleep(1)
    
    conguration(message)


##--------------------------------------------------------------------------------------------------------

    




## 31- oktiyabir soat 04:17  ti chorsu xoja ahror valiy gulbozor mfy xaqiqat kochasi




##--------------------------------------------------------------------------------------------------------


#### kop malumot olgnimizda ishlmadi malumotlar omboriga yozish uchun

## endi ishladi lokation geopoy olib yozyapturgan eakan databesga 
# shunga hato deyapturgan ekan lokation 
# str ga otkazib yozildi ALLAHGA shuku ishladi 



def conguration(message:Message):
    user_id = message.from_user.id
    user_name = message.from_user.username 

    if message.text == 'Yes ✅':



       insert_user_taxi(telegram_id = users_taxi_histiry[user_id]['user_id'], 
       contact= users_taxi_histiry[user_id]['user_contact'] ,
       taxi_sort= users_taxi_histiry[user_id]['taxi_sort'], 
       price=users_taxi_histiry[user_id]['taxi_price'],
        adress_lokation=users_taxi_histiry[user_id]['user_one_lokation'],
         adress_lokation2=users_taxi_histiry[user_id]['user_two_lokation'], 
        sitiy_distance=users_taxi_histiry[user_id]['shaxarlar_oarasidagi_masofa'])
       users_taxi_histiry.pop(user_id)   ## bu yozilgan logati boshatib qoyadi va yana boshqa malumot yozila veradi

       bot.send_message(user_id, f" MALUMOTLAR SAQALNDI ✅📃✔  ")
       menyu(message)
 
    
    elif message.text == 'No ❌':
        bot.send_message(user_id, f" MALUMOTLAR SAQLANMADI 📃❌⭕")
        menyu(message)

##--------------------------------------------------------------------------------------------------------






##--------------------------------------------------------------------------------------------------------

####  taxi standart uchun  





def one_lokation_standart(message:Message):
    global users_taxi_histiry
    user_id = message.from_user.id
    user_name = message.from_user.username
    sort_taxi = message.text
    users_taxi_histiry[user_id].update({
        'taxi_sort': sort_taxi
    })
    msg = bot.send_message(user_id, f" HURMATLI FOYDALANUVCHI LOKATSIYANGIZNI  YUBORING 📤 ",reply_markup=generate_ask_location())
    print(users_taxi_histiry)
    bot.register_next_step_handler(msg, next_two_lokation_standart)




def next_two_lokation_standart(message:Message):

    if message.content_type == 'location':

        global users_taxi_histiry
        user_id = message.from_user.id
        lat = message.location.latitude
        lon = message.location.longitude


        cordinats = (lat,lon)
        lokiation = nomainaltim.reverse(cordinats)
        print(lokiation)
        lokation_str1 = str(lokiation)


    
        # bot.send_message(user_id, f" kordinata 1 {cordinats} ")
        msg = bot.send_message(user_id, f"  HURMATLI FOYDALANUVCHI BORMOQCHI 🚶‍♂️ ⏭ BOLGAN MANZILINGIZNI LOKATSIYASINI YUBORING 📤",reply_markup=generate_ask_location())
        users_taxi_histiry[user_id].update({
            'user_one_lokation': lokation_str1
        })
        print(users_taxi_histiry)
    
        bot.register_next_step_handler(msg, show_lokation_standart,lokiation,cordinats)


    else:
        bot.send_message(user_id, f" HURMATLI FOYDALANUVCHI LOKATSIYNAGIZNI YUBORING ! ")
        one_lokation_standart(message)

    #lokatsiyani qayatarib jonatish
    # bot.send_location(user_id, lat, lon)



### ikkita loklatsiyani chiqarisah srat_taxi 



def show_lokation_standart(message:Message,lokiation,cordinats):
    global users_taxi_histiry
    user_id = message.from_user.id
    user_name = message.from_user.username
    

    lat = message.location.latitude
    lon = message.location.longitude
    cordinats2 = (lat,lon)
    print(cordinats2)
    lokiation2 = nomainaltim.reverse(cordinats2)
    
    lokation_str2 = str(lokiation2)
    
    
    # bot.send_message(user_id, f" kordinata {cordinats2} ")
    msg = bot.send_message(user_id, f" Telfon Raqamingizni Kirting 📳 : ",reply_markup= generate_ask_contact_button())
    users_taxi_histiry[user_id].update({
        'user_two_lokation': lokation_str2
    })
    print(users_taxi_histiry)
    

    bot.register_next_step_handler(msg, taxe_call_me_standart,lokiation,lokiation2,cordinats2,cordinats)








def taxe_call_me_standart(message:Message,cordinats2,cordinats,lokiation,lokiation2):
    global users_taxi_histiry
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    if message.content_type == 'contact':
        user_contact = message.contact.phone_number
        users_taxi_histiry[user_id].update({
            'user_contact': user_contact
        })
        print(users_taxi_histiry)
    elif message.content_type == 'text':
        user_contact = message.text
        users_taxi_histiry[user_id].update({
            'user_contact': user_contact
        })

    time.sleep(2)
    msg = bot.send_message(user_id, f" {user_name} ⏭⏭⏭ : > ",reply_markup=taxi_next())
    bot.register_next_step_handler(msg,sitiy_distance_standart,cordinats2,cordinats,lokiation,lokiation2)
















## orasidagi masofa hamda borishdagi narhini chiqazib beradi 

def sitiy_distance_standart(message:Message,cordinats,cordinats2,lokiation,lokiation2):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    global users_taxi_histiry

    
    #kordinatalar  lokation bilan lokation2 ga otib qolgan 

    # print(lokiation)
    # print(lokiation2)
    
    distancee = distnca_city(lokiation,lokiation2)
    print(distancee)
    pe = int(distancee)
    taxi_str = pe * 4.800
    taxi_price = str(taxi_str)

    
    users_taxi_histiry[user_id].update({
        'shaxarlar_oarasidagi_masofa': pe
    })
    print(users_taxi_histiry)


    bot.send_message(user_id, f" {user_name} SHaxarlar Orasidagi Masofa ⏭ {distancee} : {pe}.km  Taxminiy yetib  borish narxi 👉 {pe*4.800} Ming So'm 💵💲")
    users_taxi_histiry[user_id].update({
        'taxi_price': taxi_price
    })
    print(users_taxi_histiry)

    msg = bot.send_message(user_id, f" {user_name} TAXI CHAQIRILSINMI 🚖✅ ",reply_markup = generate_yes_no())


# shu yerda bir marta yozilgan show chanelga ketadi malumotlar  

    bot.register_next_step_handler(msg, show_send_chanel)












##--------------------------------------------------------------------------------------------------------








####  taxi comfort 






def one_lokation_komfort(message:Message):
    global users_taxi_histiry
    user_id = message.from_user.id
    user_name = message.from_user.username
    sort_taxi = message.text
    users_taxi_histiry[user_id].update({
        'taxi_sort': sort_taxi
    })
    msg = bot.send_message(user_id, f" HURMATLI FOYDALANUVCHI LOKATSIYANGIZNI  YUBORING 📤 ",reply_markup=generate_ask_location())
    print(users_taxi_histiry)
    bot.register_next_step_handler(msg, next_two_lokation_komfort)




def next_two_lokation_komfort(message:Message):

    if message.content_type == 'location':

        global users_taxi_histiry
        user_id = message.from_user.id
        lat = message.location.latitude
        lon = message.location.longitude


        cordinats = (lat,lon)
        lokiation = nomainaltim.reverse(cordinats)
        print(lokiation)
        lokation_str1 = str(lokiation)


    
        # bot.send_message(user_id, f" kordinata 1 {cordinats} ")
        msg = bot.send_message(user_id, f"  HURMATLI FOYDALANUVCHI BORMOQCHI 🚶‍♂️ ⏭ BOLGAN MANZILINGIZNI LOKATSIYASINI YUBORING 📤",reply_markup=generate_ask_location())
        users_taxi_histiry[user_id].update({
            'user_one_lokation': lokation_str1
        })
        print(users_taxi_histiry)
    
        bot.register_next_step_handler(msg, show_lokation_komfort,lokiation,cordinats)


    else:
        bot.send_message(user_id, f" HURMATLI FOYDALANUVCHI LOKATSIYNAGIZNI YUBORING ! ")
        one_lokation_komfort(message)


    #lokatsiyani qayatarib jonatish
    # bot.send_location(user_id, lat, lon)



### ikkita loklatsiyani chiqarisah srat_taxi 




def show_lokation_komfort(message:Message,lokiation,cordinats):
    global users_taxi_histiry
    user_id = message.from_user.id
    user_name = message.from_user.username
    

    lat = message.location.latitude
    lon = message.location.longitude
    cordinats2 = (lat,lon)
    print(cordinats2)
    lokiation2 = nomainaltim.reverse(cordinats2)
    
    lokation_str2 = str(lokiation2)
    
    
    # bot.send_message(user_id, f" kordinata {cordinats2} ")
    msg = bot.send_message(user_id, f" Telfon Raqamingizni Kirting 📳 : ",reply_markup= generate_ask_contact_button())
    users_taxi_histiry[user_id].update({
        'user_two_lokation': lokation_str2
    })
    print(users_taxi_histiry)
    

    bot.register_next_step_handler(msg, taxe_call_me_komfort,lokiation,lokiation2,cordinats2,cordinats)







## taxi calmee


def taxe_call_me_komfort(message:Message,cordinats2,cordinats,lokiation,lokiation2):
    global users_taxi_histiry
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    if message.content_type == 'contact':
        user_contact = message.contact.phone_number
        users_taxi_histiry[user_id].update({
            'user_contact': user_contact
        })
        print(users_taxi_histiry)
    elif message.content_type == 'text':
        user_contact = message.text
        users_taxi_histiry[user_id].update({
            'user_contact': user_contact
        })

    time.sleep(2)
    msg = bot.send_message(user_id, f" {user_name} ⏭⏭⏭ : > ",reply_markup=taxi_next())
    bot.register_next_step_handler(msg,sitiy_distance_komfort,cordinats2,cordinats,lokiation,lokiation2)











## orasidagi masofa hamda borishdagi narhini chiqazib beradi 

def sitiy_distance_komfort(message:Message,cordinats2,cordinats,lokiation,lokiation2):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    global users_taxi_histiry

    
    #kordinatalar  lokation bilan lokation2 ga otib qolgan 

    # print(lokiation)
    # print(lokiation2)
    
    distancee = distnca_city(lokiation,lokiation2)
    print(distancee)
    pe = int(distancee)
    taxi_str = pe * 4.800
    taxi_price = str(taxi_str)

    
    users_taxi_histiry[user_id].update({
        'shaxarlar_oarasidagi_masofa': pe
    })
    print(users_taxi_histiry)


    bot.send_message(user_id, f" {user_name} SHaxarlar Orasidagi Masofa ⏭ {distancee} : {pe}.km  Taxminiy yetib  borish narxi 👉 {pe*4.800} Ming So'm 💵💲")
    users_taxi_histiry[user_id].update({
        'taxi_price': taxi_price
    })
    print(users_taxi_histiry)

    msg = bot.send_message(user_id, f" {user_name} TAXI CHAQIRILSINMI 🚖✅ ",reply_markup = generate_yes_no())


# shu yerda bir marta yozilgan show chanelga ketadi malumotlar  

    bot.register_next_step_handler(msg, show_send_chanel)









##--------------------------------------------------------------------------------------------------------

##  taxi  biznes  





def one_lokation_biznes(message:Message):
    global users_taxi_histiry
    user_id = message.from_user.id
    user_name = message.from_user.username
    sort_taxi = message.text
    users_taxi_histiry[user_id].update({
        'taxi_sort': sort_taxi
    })
    msg = bot.send_message(user_id, f" HURMATLI FOYDALANUVCHI LOKATSIYANGIZNI  YUBORING 📤 ",reply_markup=generate_ask_location())
    print(users_taxi_histiry)
    bot.register_next_step_handler(msg, next_two_lokation_biznes)




def next_two_lokation_biznes(message:Message):
    if message.content_type == 'location':

        global users_taxi_histiry
        user_id = message.from_user.id
        lat = message.location.latitude
        lon = message.location.longitude


        cordinats = (lat,lon)
        lokiation = nomainaltim.reverse(cordinats)
        print(lokiation)
        lokation_str1 = str(lokiation)


    
        # bot.send_message(user_id, f" kordinata 1 {cordinats} ")
        msg = bot.send_message(user_id, f"  HURMATLI FOYDALANUVCHI BORMOQCHI 🚶‍♂️ ⏭ BOLGAN MANZILINGIZNI LOKATSIYASINI YUBORING 📤",reply_markup=generate_ask_location())
        users_taxi_histiry[user_id].update({
            'user_one_lokation': lokation_str1
        })
        print(users_taxi_histiry)
    
        bot.register_next_step_handler(msg, show_lokation_biznes,lokiation,cordinats)


    else:
        bot.send_message(user_id, f" HURMATLI FOYDALANUVCHI LOKATSIYNAGIZNI YUBORING ! ")
        one_lokation_biznes(message)


    #lokatsiyani qayatarib jonatish
    # bot.send_location(user_id, lat, lon)



### ikkita loklatsiyani chiqarisah srat_taxi 




def show_lokation_biznes(message:Message,lokiation,cordinats):
    global users_taxi_histiry
    user_id = message.from_user.id
    user_name = message.from_user.username
    

    lat = message.location.latitude
    lon = message.location.longitude
    cordinats2 = (lat,lon)
    print(cordinats2)
    lokiation2 = nomainaltim.reverse(cordinats2)
    
    lokation_str2 = str(lokiation2)
    
    
    # bot.send_message(user_id, f" kordinata {cordinats2} ")
    msg = bot.send_message(user_id, f" Telfon Raqamingizni Kirting 📳 : ",reply_markup= generate_ask_contact_button())
    users_taxi_histiry[user_id].update({
        'user_two_lokation': lokation_str2
    })
    print(users_taxi_histiry)
    

    bot.register_next_step_handler(msg, taxe_call_me_biznes,lokiation,lokiation2,cordinats2,cordinats)








### nomerini olish 


def taxe_call_me_biznes(message:Message,cordinats2,cordinats,lokiation,lokiation2):
    global users_taxi_histiry
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    if message.content_type == 'contact':
        user_contact = message.contact.phone_number
        users_taxi_histiry[user_id].update({
            'user_contact': user_contact
        })
        print(users_taxi_histiry)
    elif message.content_type == 'text':
        user_contact = message.text
        users_taxi_histiry[user_id].update({
            'user_contact': user_contact
        })

    time.sleep(2)
    msg = bot.send_message(user_id, f" {user_name} ⏭⏭⏭ : > ",reply_markup=taxi_next())
    bot.register_next_step_handler(msg,sitiy_distance_biznes,cordinats2,cordinats,lokiation,lokiation2)





## orasidagi masofa hamda borishdagi narhini chiqazib beradi 

def sitiy_distance_biznes(message:Message,cordinats2,cordinats,lokiation,lokiation2):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    global users_taxi_histiry

    
    #kordinatalar  lokation bilan lokation2 ga otib qolgan 

    # print(lokiation)
    # print(lokiation2)
    
    distancee = distnca_city(lokiation,lokiation2)
    print(distancee)
    pe = int(distancee)
    taxi_str = pe * 4.800
    taxi_price = str(taxi_str)

    
    users_taxi_histiry[user_id].update({
        'shaxarlar_oarasidagi_masofa': pe
    })
    print(users_taxi_histiry)


    bot.send_message(user_id, f" {user_name} SHaxarlar Orasidagi Masofa ⏭ {distancee} : {pe}.km  Taxminiy yetib  borish narxi 👉 {pe*4.800} Ming So'm 💵💲")
    users_taxi_histiry[user_id].update({
        'taxi_price': taxi_price
    })
    print(users_taxi_histiry)

    msg = bot.send_message(user_id, f" {user_name} TAXI CHAQIRILSINMI 🚖✅ ",reply_markup = generate_yes_no())


# shu yerda bir marta yozilgan show chanelga ketadi malumotlar  

    bot.register_next_step_handler(msg, show_send_chanel)






















# bot.polling(none_stop=True)
bot.infinity_polling()

# bot.polling(timeout=600)


# bot.polling(timeout=600)

