
"""
2.1 Связи между таблицами
https://stepik.org/lesson/308885/step/1?unit=291011
"""

import psycopg2
from variables_2_1 import table_name, data_book, auth_data

# Connect to an existing database
conn = psycopg2.connect(**auth_data)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute(f"CREATE TABLE {table_name} (book_id serial PRIMARY KEY, title VARCHAR(50), name_author VARCHAR(50), "
            f"price DECIMAL(8,2), amount integer);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
for i in data_book:
    print(type(i), i)
    cur.execute(f"INSERT INTO {table_name} (title, name_author, price, amount) "
                f"VALUES {i};")

# Query the database and obtain data as Python objects
cur.execute(f"SELECT * FROM {table_name};")
print(cur.fetchall())

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
