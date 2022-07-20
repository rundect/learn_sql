
"""
2.1 Связи между таблицами
Связь «один ко многим»
https://stepik.org/lesson/308885/step/2?unit=291011
"""

import psycopg2
from variables_2_1 import data_name_author, auth_data

table_name = 'author1'

conn = psycopg2.connect(**auth_data)
cur = conn.cursor()

cur.execute(f"CREATE TABLE {table_name} (author_id serial PRIMARY KEY, name_author VARCHAR(50));")
for i in data_name_author:
    cur.execute(f"INSERT INTO {table_name} (name_author) VALUES {i};")


cur.execute(f"SELECT * FROM {table_name};")
print(cur.fetchall())

conn.commit()
cur.close()
conn.close()
