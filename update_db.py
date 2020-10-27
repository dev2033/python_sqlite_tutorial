"""
Изменение данных в БД, Здесь вы можете использовать команду SET, чтобы
изменить поле, так что в нашем случае мы изменим имя исполнителя на
John Doe в каждой записи, где поле исполнителя указано для Andy Hunter.
"""
import sqlite3


conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

sql = """
UPDATE albums
SET artist = 'John Doe'
WHERE artist = 'Andy Hunter'
"""

cursor.execute(sql)
conn.commit()
