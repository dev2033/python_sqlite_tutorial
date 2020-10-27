"""
Удаление значений из таблицы в БД
В данном случае удаляем из поля artist значения 'John Doe'
"""
import sqlite3


conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

sql = "DELETE FROM albums WHERE artist = 'John Doe'"

cursor.execute(sql)
conn.commit()
