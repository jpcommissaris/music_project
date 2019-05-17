# goal of this file is to connect any database to python and be able to use it
import psycopg2

# establish the connection
def connect():
    """ Connect to the PostgreSQL database server """
    host = "127.0.0.1"
    db = "template1"
    user = "JulianC"
    port = 5432
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host=host, database=db, user=user)
        print("connection successful\n")
        execute(conn)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

# heres where we can put SQL commands inside a cursor object
# execute('sequel code') executes the code, fetchone() gets the result
def execute(conn):

    cur = conn.cursor()
    # tester: get db version
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    version = cur.fetchone()
    print(version)


    cur.close()

# run
if __name__ == '__main__':
    connect()
