"""
Добавление данных в таблицу orders
"""

import sqlite3


conn = sqlite3.connect('orders.db')
cur = conn.cursor()

data = [('01', 'today', '2', 'many'), ('02', 'today', '3', 'many')]

cur.executemany("INSERT INTO orders VALUES(?, ?, ?, ?);", data)
conn.commit()


