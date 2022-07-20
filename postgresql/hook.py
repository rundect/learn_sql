import psycopg2

# Connect to an existing database
conn = psycopg2.connect(
    dbname="test",
    user="admin",
    password="secret",
    host="localhost",
    port="5432"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
n = input("Введите число: ")
print(n)
cur.execute(f"INSERT INTO genre (name_genre) VALUES ({n})")

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM genre;")
cur.fetchone()  # ("100")
print(cur)
# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()