"""
2.1 Связи между таблицами
https://stepik.org/lesson/308885/step/1?unit=291011
"""
auth_data = {'dbname': 'test', 'user': 'admin', 'password': 'secret', 'host': 'localhost', 'port': '5432'}
table_name = "book"
data_book = [('Мастер и Маргарита', 'Булгаков М.А.', 670.99, 3),
             ('Белая гвардия', 'Булгаков М.А.', 540.50, 5),
             ('Идиот', 'Достоевский Ф.М.', 460.00, 10),
             ('Братья Карамазовы', 'Достоевский Ф.М.', 799.01, 2),
             ('Стихотворения и поэмы', 'Есенин С.А.', 650.00, 15)]

data_name_author = ("('Булгаков М.А.')",
                    "('Достоевский Ф.М.')",
                    "('Есенин С.А.')",
                    "('Пастернак Б.Л.')",
                    )
