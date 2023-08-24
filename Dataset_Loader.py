import psycopg2
from psycopg2 import sql
import random

def load_data():
    connection = psycopg2.connect(
        user="postgres",
        password="joelbunyan",
        host="localhost",
        port="5432"
    )

    connection.autocommit = True
    cursor = connection.cursor()

    database_name = "Finance---database"
    create_db_query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database_name))
    cursor.execute(create_db_query)
    print("Database created successfully!")

    connection.close()  
    connection = psycopg2.connect(
        user="postgres",
        password="joelbunyan",
        host="localhost",
        port="5432",
        dbname=database_name  
    )
    cursor = connection.cursor()

    
    create_table_query = """
    CREATE TABLE table1 (
        month VARCHAR(255),
        salary INT,
        saving INT
    );
    """
    cursor.execute(create_table_query)

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    salary = 100000
    query = """
    INSERT INTO table1 (month, salary, saving)
    VALUES (%s, %s, %s);
    """
    for month in months:
        expenditure = random.randint(10000, 80000)
        saving = salary - expenditure
        data = (month, salary, saving)
        cursor.execute(query, data)

    connection.commit()
    cursor.close()
    connection.close()

