import psycopg2
import csv
from config import load_config

def execute_query(sql, params=None, fetch=False):
    """Универсальная функция для работы БД"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                if fetch:
                    return cur.fetchall()
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS phonebook (
        contact_id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(20) NOT NULL
    )
    """
    execute_query(sql)
    print("Table created/verified.")

def insert_from_csv(filename):
    with open(filename, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            sql = "INSERT INTO phonebook(name, phone) VALUES(%s, %s)"
            execute_query(sql, (row[0], row[1]))
    print(f"Data imported from {filename}")

def add_contact(name, phone):
    sql = "INSERT INTO phonebook(name, phone) VALUES(%s, %s)"
    execute_query(sql, (name, phone))
    print(f"Contact {name} added.")

def update_contact(name, new_phone):
    sql = "UPDATE phonebook SET phone = %s WHERE name = %s"
    execute_query(sql, (new_phone, name))
    print(f"Contact {name} updated.")

def query_contacts(pattern):
    sql = "SELECT * FROM phonebook WHERE name LIKE %s OR phone LIKE %s"
    results = execute_query(sql, (f'%{pattern}%', f'%{pattern}%'), fetch=True)
    for row in results:
        print(row)

def delete_contact(name):
    sql = "DELETE FROM phonebook WHERE name = %s"
    execute_query(sql, (name,))
    print(f"Contact {name} deleted.")

if __name__ == "__main__":
    
    create_table()
    insert_from_csv('contacts.csv')
    
    # Примеры работы
    add_contact('Meirlan', '87770001122')
    update_contact('Ivan', '89990000000')
    print("Search results for 'Alibi':")
    query_contacts('Alibi')
    delete_contact('Ivan')