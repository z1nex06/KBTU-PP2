# this code from tutorial
# https://neon.com/postgresql/postgresql-python/connect

import psycopg2

def connect():
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(host="localhost",database="PhoneBook",user="Meirlan",password="12345678", options="") as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    connect()