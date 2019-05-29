# goal of this file is to connect any database to python and be able to use it
# USAGE: change the CONST parameters in connect to match your database, Use the execute function to execute sql code
import psycopg2
from scrap import Scrapper


# establish the connection
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
def execute(conn):
    # tester code, does nothing for project
    cur = conn.cursor()
    cur.execute("CREATE TABLE " + "IF NOT EXISTS " + "sample_table " + "(song VARCHAR);")
    cur.execute("INSERT INTO " + "sample_table" + "(song)" + "VALUES('hello');")
    cur.close()


def dumpV3(conn):
    cur = conn.cursor()
    # --- drop table ---
    cur.execute("DROP TABLE IF EXISTS popularity;")
    cur.execute("DROP TABLE IF EXISTS songs;")
    print("--> Cleared tables")

    # --- create tables ---
    table_commands = "(id SERIAL NOT NULL, title text NOT NULL, artist text NOT NULL ,PRIMARY KEY (id), UNIQUE(title, artist));"
    cur.execute("CREATE TABLE songs" + table_commands)
    print("--> Created songs table")
    table_commands = "(songId integer REFERENCES Songs(id),year integer NOT NULL, rank integer NOT NULL, PRIMARY KEY (songId, year), UNIQUE(songId, year), UNIQUE(year, rank));"
    cur.execute("CREATE TABLE popularity" + table_commands)
    print("--> Created popularity table")

    # --- top100 years data ---
    for year in range(2005, 2010):
        # -- load data --
        url = 'http://billboardtop100of.com/' + str(year) + '-2/'
        s = Scrapper(url) # loads object
        s.get_rows_SQL() # puts songs into s.table, type: array
        # loop through songs
        for song in s.table:
            # -- insert into songs table --
            inserts = "INSERT INTO songs(title, artist)"
            values = "VALUES(" "'" + song.song + "', " + "'" + song.artist + "'" + ")"
            cur.execute(inserts + values + " ON CONFLICT(title, artist) DO NOTHING;")
            # -- insert into popularity table --
            inserts = "INSERT INTO popularity(songID, year, rank)"
            values = "((SELECT id from songs WHERE title = '%s' AND artist = '%s'), %s, %s )"\
                     % (song.song, song.artist, str(year), song.rank)
            cur.execute(inserts + "Values" + values + " ON CONFLICT DO NOTHING;")
        print("Added top100 songs for year ", year)
    cur.close()
    conn.commit()
    print("changes committed")


def info(conn):
    cur = conn.cursor()
    # -- run executes to gain info --
    print("Running information methods: ")

    # ---> here is where executes go
    cur.execute("select * from popularity ORDER BY songid, year ASC;")
    # cur.execute("select * from popularity ORDER BY rank, songid ASC;")
    # ---> end

    # -- iterate and print --
    for song in cur:
        print(song) # cur object is iterable
    cur.close()
    print("All Info printed")


# run script, must set parameters if not using defaults
if __name__ == '__main__':
    connect(db="music", user="JulianC")


