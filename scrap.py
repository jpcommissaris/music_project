import requests
import lxml.html as lh
import pandas as pd

# this class gets the data off billboards top100
class Scrapper:
    def __init__(self, url):
        # parameters
        self.url = url
        # instance vars
        self.row_data = None
        self.content = None
        self.table = []

    # -- returns the scrapped data as a Pandas DataFrame
    def getFrame(self):
        dic = {title: column for (title, column) in self.table}
        frame = pd.DataFrame(dic)
        return frame

    # helper functions
    def getHeader(self):
        # gets first row
            self.table.append(("RANK", []))
            self.table.append(("ARTIST", []))
            self.table.append(("SONG", []))

    def set_tag(self, tag):
        page = requests.get(self.url)
        self.content = lh.fromstring(page.content)
        self.row_data = self.content.xpath(tag)  # gets data inside a tag

    def setTableB(self, tag='//tr'):
        self.set_tag(tag)
        self.getHeader()
        self.getRowsB()

    def get_rows_SQL(self, tag='//tr'):
        self.set_tag(tag)
        self.getTable()

    def getTable(self):
        # fills remaining rows
        num = int(len(self.row_data)-1)
        for r in range(0, num): #
            arg = []
            T = self.row_data[r] # current row
            i = 0 # current column
            for t in T.iterchildren():
                data = t.text_content()
                arg.append(data)
            s = Song(arg[0], arg[1], arg[2])
            self.table.append(s)


    def getRowsB(self):
        # fills remaining rows
        num = int(len(self.row_data)-1)
        for r in range(0, num): #
            T = self.row_data[r] # current row
            i = 0 # current column
            for t in T.iterchildren():
                data = t.text_content()
                self.table[i][1].append(data)
                i += 1

# -- object that holds song info --
class Song:

    def __init__(self, rank, song, artist):
        self.rank = rank
        self.song = song
        self.artist = artist

    # -- override toString --
    def __str__(self):
        return f'Rank: {self.rank}, artist: {self.artist}, Song: {self.song}'


