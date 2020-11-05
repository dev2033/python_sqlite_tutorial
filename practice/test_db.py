"""
Создание таблицы test.db

Данный скрипт создаёт таблицу Cars и вставляет 8 строк в таблицу.

>> cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")

Этот SQL-запрос создает новую таблицу Cars. Таблица имеет три столбца.


Мы проверяем записанные данные консольным инструментом sqlite3. 
В первую очередь, мы изменяем способ, которым данные отображаются в консоли. 
Мы используем режим столбцов и включаем заголовки.

sqlite> .mode column  
sqlite> .headers on
sqlite> SELECT * FROM Cars;

Вывод:

Id          Name        Price     
----------  ----------  ----------
1           Audi        52642     
2           Mercedes    57127     
3           Skoda       9000      
4           Volvo       29000     
5           Bentley     350000    
6           Citroen     21000     
7           Hummer      41400     
8           Volkswagen  21600
"""
import sqlite3 as lite
import sys
 
 
# Подключаемся к базе данных
con = lite.connect('test.db')
 
with con:
    cur = con.cursor()    
    # Создаем таблицу
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    # Вносим данные
    cur.execute("INSERT INTO Cars VALUES(1, 'Audi', 52642)")
    cur.execute("INSERT INTO Cars VALUES(2, 'Mercedes', 57127)")
    cur.execute("INSERT INTO Cars VALUES(3, 'Skoda', 9000)")
    cur.execute("INSERT INTO Cars VALUES(4, 'Volvo', 29000)")
    cur.execute("INSERT INTO Cars VALUES(5, 'Bentley', 350000)")
    cur.execute("INSERT INTO Cars VALUES(6, 'Citroen', 21000)")
    cur.execute("INSERT INTO Cars VALUES(7, 'Hummer', 41400)")
    cur.execute("INSERT INTO Cars VALUES(8, 'Volkswagen', 21600)")
