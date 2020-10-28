"""
1) Использование fetchone() в SQLite в Python:
    Функция fetchone() - получает только один объект
2) Использование fetchmany() в SQLite в Python:
    Функция fetchmany() - получает несколько объектов (много данных)
3) Использование fetchall() в SQLite в Python:
    Функция fetchall() - получает все результаты(все объекты таблицы)
"""

import sqlite3


conn = sqlite3.connect('orders.db')
cur = conn.cursor()

# Выводит один элемент
cur.execute("SELECT * FROM users;")
one_result = cur.fetchone()
print(one_result)

# Выводит несколько элементов (в данном случае - 2)
cur.execute("SELECT * FROM users;")
two_results = cur.fetchmany(2)
print(two_results)

# Выводит все элементы
cur.execute("SELECT * FROM users;")
all_results = cur.fetchall()
print(all_results)

