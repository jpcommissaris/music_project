# goal of this file is to connect any database to python and be able to use it
# USAGE: change the CONST parameters in connect to match your database, Use the execute function to execute sql code
import psycopg2
from scrap import Scrapper

# establish the connection
def connect():
    """ Connect to the PostgreSQL database server """
    HOST = "127.0.0.1"
    DB = "music"
    USER = "JulianC"
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host=HOST, database=DB, user=USER)
        print("connection successful\n")
        # ---> here is where functions can go to update the database --->
        #execute(conn)
        dirtyDump(conn)
        # end changes and commit <---
        conn.commit()
        print("changes committed")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: ", error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

# heres where we can put SQL commands inside a cursor object
# Documentation for Cursor class:   http://initd.org/psycopg/docs/cursor.html
# psql commands:  http://www.postgresqltutorial.com/psql-commands/
def execute(conn):

    cur = conn.cursor()

    # tester: get db version
    print('PostgreSQL database version:')
    cur.execute("CREATE TABLE " + "IF NOT EXISTS " + "sample_table " + "(song VARCHAR);")
    cur.execute("INSERT INTO " + "sample_table" + "(song)" + "VALUES('hello');")

    cur.close()


def dirtyDump(conn):
    cur = conn.cursor()
    for year in range(1970, 2010):
        table_name = "t"+str(year)
        cur.execute("DROP TABLE IF EXISTS " + table_name + ";")
        cur.execute("CREATE TABLE " + table_name + "(song VARCHAR, artist VARCHAR, rank INT);")
        url = 'http://billboardtop100of.com/' + str(year) + '-2/'
        s = Scrapper(url)
        s.get_rows_SQL()
        for song in s.table:
            inserts = "INSERT INTO " + table_name + "(song, artist, rank)"
            values = "VALUES(" + "'" + song.song + "', " + "'" + song.artist + "', " + "'" + song.rank + "'" + ");"
            cur.execute(inserts + values)
            #print(inserts, "\n", values)

        print(year)
    cur.close()

# run
if __name__ == '__main__':
    connect()