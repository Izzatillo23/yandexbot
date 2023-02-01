import sqlite3

database = sqlite3.connect("yandex.db")
cursor = database.cursor()


def create_users_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS yandex_user(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id BIGINT UNIQUE,
        full_name TEXT,
        contact TEXT,
        pasword TEXT

    )
    """)


create_users_table()
database.commit()
database.close()









####  taxilar tarihi uchun



database = sqlite3.connect("yandex_taxi.db")
cursor = database.cursor()


def create_taxi_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS yandex_taxi_sort(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id BIGINT ,
        contact TEXT,
        taxi_sort TEXT,
        price TEXT,
        adress_lokation TEXT,
        adress_lokation2 TEXT,
        sitiy_distance TEXT


    )
    """)


create_taxi_table()
database.commit()
database.close()
















