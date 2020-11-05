"""
Запросы с параметрами

Мы обновляем цену одной машины. В этом примере кода, 
мы используем заполнители типа «знак вопроса».

Знаки вопроса ? являются заполнителями для значений. 
Значения добавляются на его место.

Свойство rowcount возвращает количество обновленных строк. 
В нашем случае, одна строка была обновлена.

Вводим в терминал:
sqlite3 test.db

Затем в консоли sqlite вводим следующее:

sqlite> .mode column  
sqlite> .headers on
sqlite> SELECT * FROM Cars;

Вывод:

Id          Name        Price     
----------  ----------  ----------
1           Audi        62300     
2           Mercedes    57127     
3           Skoda       9000      
4           Volvo       29000     
5           Bentley     350000    
6           Citroen     21000     
7           Hummer      41400     
8           Volkswagen  21600

Как можно заметить изменился Price у Id = 1 с name = Audi
"""
import sqlite3 as lite
import sys


uId = 1
uPrice = 62300 
 
con = lite.connect('test.db')
with con:
    cur = con.cursor()    
    cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))        
    con.commit()
    print("Number of rows updated: %d" % cur.rowcount)
