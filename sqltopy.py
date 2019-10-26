"""Use SQL database to store songs scrapped from billboards"""
# USAGE: change the CONST parameters in connect to match your database, Use the execute function to execute sql code
import psycopg2
from scrap import Scrapper

# -- establish a connection to SQL database --
def connect(db="music", user="JuliaC", host="127.0.0.1", port=5432):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host=host, database=db, user=user, port=port)
        print("connection successful\n")

        # ---> here is where functions can go to update or scan the database
        dumpV3(conn)
        info(conn)
        # ---> end

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: ", error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


# heres where we can put SQL commands inside a cursor object
# Documentation for Cursor class:   http://initd.org/psycopg/docs/cursor.html
# psql commands:  http://www.postgresqltutorial.com/psql-commands/


# -- take songs off buildboards and place them into database
def dumpV3(conn):
    cur = conn.cursor()

    # --- drop tables ---
    cur.execute("DROP TABLE IF EXISTS popularity;")
    cur.execute("DROP TABLE IF EXISTS songs;")
    print("--> Cleared tables")

    # --- create song table ---
    table_commands = "(id SERIAL NOT NULL, title text NOT NULL, artist text NOT NULL ,PRIMARY KEY (id), UNIQUE(title, artist));"
    cur.execute("CREATE TABLE songs" + table_commands)
    print("--> Created songs table")
    table_commands = "(songId integer REFERENCES Songs(id),year integer NOT NULL, rank integer NOT NULL, PRIMARY KEY (songId, year), UNIQUE(songId, year), UNIQUE(year, rank));"

    # --- top100 years data ---
    for year in range(1980, 2016):
        # -- load data --
        url = 'http://billboardtop100of.com/' + str(year) + '-2/'
        s = Scrapper(url)
        s.get_rows_SQL() # puts songs into s.table, type: array
        # loop through songs
        for song in s.table:
            # -- insert into songs table --
            inserts = "INSERT INTO songs(title, artist)"
            values = "VALUES(" "'" + song.song + "', " + "'" + song.artist + "'" + ")"
            cur.execute(inserts + values + " ON CONFLICT(title, artist) DO NOTHING;")
        print("Added top100 songs for year ", year)
    cur.close()
    conn.commit()
    print("changes committed")


def info(conn):
    cur = conn.cursor()
    # -- run executes to gain info --
    print("Running information methods: ")
    cur.execute("select * from song ORDER BY songid, year ASC;")

    # -- iterate and print --
    for song in cur:
        print(song) # cur object is iterable
    cur.close()


# run script, must set parameters if not using defaults
if __name__ == '__main__':
    connect(db="music", user="JulianC")


