from faker import Faker
import psycopg2

# Replace the connection details with your Render PostgreSQL connection string
connection_string = "postgres://root:4fDCwsuZZCgowihAQzNLmTzeyeaoyppQ@dpg-cmkr88en7f5s73au5ol0-a.oregon-postgres.render.com/analyst_database"

# Connect to PostgreSQL using the provided connection string
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()

fake = Faker()
create_table_query = '''
    CREATE TABLE analyst (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER,
        workinghours INTEGER,
        salary INTEGER,
        city VARCHAR(100)
);
'''

# Execute the SQL script to create the table
cursor.execute(create_table_query)

# Generate and insert 100 rows of random data
for i in range(1, 101):
    name = fake.name()
    age = fake.random_int(min=20, max=60)
    workinghours = fake.random_int(min=30, max=50)
    salary = fake.random_int(min=40000, max=90000)
    city = fake.city()

    cursor.execute(
        "INSERT INTO analyst (id, name, age, workinghours, salary, city) VALUES (%s, %s, %s, %s, %s, %s)",
        (i, name, age, workinghours, salary, city)
    )

# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()
