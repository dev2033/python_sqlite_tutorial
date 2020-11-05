"""
Вывод данных из БД
"""
import sqlite3 as lite
import sys


con = lite.connect('orders.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    print(rows)


with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users")

    while True:
        row = cur.fetchone()
        if row == None:
            break
        print(row[0], row[1], row[2])
