# goal of this file is to connect any database to python and be able to use it
# USAGE: change the CONST parameters in connect to match your database, Use the execute function to execute sql code
import psycopg2

# establish the connection
def connect():
    """ Connect to the PostgreSQL database server """
    HOST = "127.0.0.1"
    DB = "template1"
    USER = "JulianC"
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host=HOST, database=DB, user=USER)
        print("connection successful\n")
        execute(conn)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

# heres where we can put SQL commands inside a cursor object
# Documentation for Cursor class:   http://initd.org/psycopg/docs/cursor.html
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