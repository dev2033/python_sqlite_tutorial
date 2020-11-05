"""
Добавление картинки в базу данных
В терминале вводим:
    sqlite3 load_img.db
Затем открывается консоль sqlite. В ней создаем таблицу:
    sqlite> CREATE TABLE Images(Id INTEGER PRIMARY KEY, Data BLOB);
Запускаем скрипт еще раз
"""
import sqlite3 as lite
import sys


def readImage(filename):
    """Функция открытия изображения в бинарном режиме"""
    try:
        fin = open('images/arnold.png', "rb")
        img = fin.read()
        return img
        
    except IOError as e:
        # В случае ошибки, выводим ее текст
        print("Error %d: %s" % (e.args[0],e.args[1]))
        sys.exit(1)
 
    finally:
        if fin:
            # Закрываем подключение с файлом
            fin.close()
 
try:
    # Открываем базу данных
    con = lite.connect('load_img.db')
    cur = con.cursor()
    # Получаем бинарные данные нашего файла
    data = readImage("images/arnold.png")
    # Конвертируем данные
    binary = lite.Binary(data)
    # Готовим запрос в базу
    cur.execute("INSERT INTO Images(Data) VALUES (?)", (binary,) )
    # Выполняем запрос
    con.commit()    
    
# В случаи ошибки выводим ее текст.
except lite.Error as e:
    if con:
        con.rollback()
        
    print("Error %s:" % e.args[0])
    sys.exit(1)
    
finally:
    if con:
    # Закрываем подключение с базой данных
        con.close()