"""
Удаление данных в SQLite в Python
"""

import sqlite3


conn = sqlite3.connect('orders.db')
cur = conn.cursor()

# Из таблицы users, из поля lname - удаляем Parker
cur.execute("DELETE FROM users WHERE lname='Parker';")
conn.commit()
