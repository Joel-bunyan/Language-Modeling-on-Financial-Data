import psycopg2
from psycopg2 import sql

try:
    connection = psycopg2.connect(
        user="postgres",
        password="joelbunyan",
        host="localhost",
        port="5432"
    )
    
    connection.autocommit = True

    cursor = connection.cursor()

except psycopg2.Error as e:
    print("Error while connecting to PostgreSQL:", e)
    exit()

try:
    database_name = "Finance data"
    create_db_query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database_name))
    cursor.execute(create_db_query)
    print("Database created successfully!")

except psycopg2.Error as e:
    print("Error while creating database:", e)

finally:
    cursor.close()
    connection.close()
