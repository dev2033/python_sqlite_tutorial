"""
Практика работы с БД в Python. В данном случает это SQLite3
Шаги действий в коде:
    1. Присоединяем БД
    2. Создаем 2 таблицы:
        1) users
        2) orders
    3. Заполняем данными таблицу users:
        1) В первом случае мы заполняем один кортеж данными методом execute
        2) Во втором случае заполняем двумя кортежами с данными
            из 4х элементов, методом executemany
"""

import sqlite3


conn = sqlite3.connect('orders.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   orderid INT PRIMARY KEY,
   date TEXT,
   userid TEXT,
   total TEXT);
""")
conn.commit()

user = ('00002', 'Lois', 'Lane', 'Female')

cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
conn.commit()

more_users = [('00003', 'Peter', 'Parker', 'Male'), ('00004', 'Bruce', 'Wayne', 'male')]

cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)
conn.commit()

