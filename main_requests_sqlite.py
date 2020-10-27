"""
Основные запросы:
    1. Первый запрос, который мы выполнили, называется SELECT *,
    что означает, что мы хотим выбрать все записи, подходящие под
    переданное имя исполнителя, в нашем случае это “Red”.
    2. Далее мы выполняем SQL и используем функцию fetchall()
    для получения результатов. Вы также можете использовать функцию
    fetchone() для получения первого результата. Обратите внимание на то,
    что здесь есть прокомментированный раздел, связанный с таинственным row_factory.
    Если вы не прокомментируете эту строку, результат вернется, так как объекты Row,
    подобны словарям Python и дают вам доступ к полям строк точь в точь, как и словарь.
    В любом случае, вы не можете выполнить назначение пункта, используя объект Row.
    3. Второй запрос очень похож на первый, но возвращает каждую запись в базе
    данных и упорядочивает результаты по имени артиста в порядке возрастания.
    Это также показывает, как мы можем зациклить результаты выдачи.
    4. Последний запрос показывает, как команда LIKE используется при поиске частичных фраз.
    В нашем случае, мы искали по всей таблице заголовки, которые начинаются с
    артикля The.
    Знак процента (%) является подстановочным оператором.
"""
import sqlite3


conn = sqlite3.connect("mydatabase.db")
#conn.row_factory = sqlite3.Row
cursor = conn.cursor()
# 1
sql = "SELECT * FROM albums WHERE artist=?"
cursor.execute(sql, [("Red")])
print(cursor.fetchall()) # or use fetchone()
# 3
print("Here's a listing of all the records in the table:")
for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
    print(row)

print("Results from a LIKE query:")
# 4
sql = "SELECT * FROM albums WHERE title LIKE 'The%'"
cursor.execute(sql)

print(cursor.fetchall())
