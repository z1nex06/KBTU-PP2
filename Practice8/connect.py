import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="PhoneBook",
        user="postgres",
        password="5939",
        client_encoding="UTF8"
    )