
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


def dumpV2(conn):
    cur = conn.cursor()
    table_name = "songs"
    cur.execute("DROP TABLE IF EXISTS " + table_name + ";")  # can get rid of once preventing duplicates works
    table_commands = "(id SERIAL NOT NULL, title text NOT NULL, artist text NOT NULL ,PRIMARY KEY (id), UNIQUE(title, artist));"
    cur.execute("CREATE TABLE " + table_name + table_commands)

    # add loop here
    for year in range(2005, 2010):
        url = 'http://billboardtop100of.com/' + str(year) + '-2/'
        s = Scrapper(url)
        s.get_rows_SQL()
        for song in s.table:
            inserts = "INSERT INTO " + table_name + "(title, artist)"
            values = "VALUES(" "'" + song.song + "', " + "'" + song.artist + "'" + ")"
            cur.execute(inserts + values + " ON CONFLICT(title, artist) DO NOTHING;")
            # print(inserts, "\n", values)
        print(year)
    cur.close()