# Ma'lumotlar bazasiga jo'natiladigan so'rovlar uchun
import sqlite3


def insert_user(telegram_id, full_name, contact,pasword):
    database = sqlite3.connect("yandex.db")
    cursor = database.cursor()
    cursor.execute("""
    INSERT INTO yandex_user(telegram_id, full_name, contact,pasword)
    VALUES (?,?,?,?)
    """, (telegram_id, full_name, contact,pasword))
    database.commit()
    database.close()


def get_all_users():
    database = sqlite3.connect("yandex.db")
    cursor = database.cursor()
    cursor.execute("""
        SELECT telegram_id FROM yandex_user
        """)
    users_ids = cursor.fetchall()
    database.close()
    users = []
    # [(1234567890,), (9876543210,)] ---> [1234567890, 9876543210]

    for user in users_ids:
        users.append(user[0])

    return users





### pasword uchuun


def get_pasword(telegram_id,pasword):
    database = sqlite3.connect('yandex.db')
    cursor = database.cursor()
    cursor.execute("""

      SELECT *  FROM yandex_user
      WHERE telegram_id = ?
      AND pasword = ? 
      
    """,(telegram_id,pasword))

    user_pasword = cursor.fetchone()
    return user_pasword
    


    








def get_all_users_chanel():
    database = sqlite3.connect("yandex.db")
    cursor = database.cursor()
    cursor.execute("""
        SELECT telegram_id , full_name ,contact , pasword FROM yandex_user
        """)
    users_ids = cursor.fetchall()
    database.close()

    return users_ids







### malumotlar user


def get_user_shaxsiy(telegram_id):
    database = sqlite3.connect('yandex.db')
    cursor = database.cursor()
    cursor.execute("""

      SELECT telegram_id , full_name ,contact , pasword FROM yandex_user
      WHERE telegram_id = ?

      
    """,(telegram_id,))

    user_makumotlar = cursor.fetchall()
    return user_makumotlar








### taxi historiya uchun  foydalanuvchi uchun historiya chaqirilgan taxilar



def insert_user_taxi(telegram_id,  contact,taxi_sort,price,adress_lokation,adress_lokation2,sitiy_distance):
    database1 = sqlite3.connect("yandex_taxi.db")
    cursor = database1.cursor()
    cursor.execute("""
    INSERT INTO yandex_taxi_sort(telegram_id, contact,taxi_sort, price ,adress_lokation,adress_lokation2,sitiy_distance)
    VALUES (?,?,?,?,?,?,?)
    """, (telegram_id, contact,taxi_sort,price,adress_lokation,adress_lokation2,sitiy_distance))
    database1.commit()











### histiryga 

def  select_historiy(tg_id):
    database = sqlite3.connect('yandex_taxi.db')
    cursor = database.cursor()

    cursor.execute("""
    SELECT contact,taxi_sort,price,adress_lokation,adress_lokation2,sitiy_distance
    FROM yandex_taxi_sort 
    WHERE telegram_id = ?
                  """,(tg_id,))

    traslates = cursor.fetchall()
    
    database.close()

    return traslates