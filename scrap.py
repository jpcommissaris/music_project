import requests
import lxml.html as lh
import pandas as pd


class Scrapper:

    def __init__(self, url):
        # parameters
        self.url = url
        # instance vars
        self.row_data = None
        self.content = None
        self.table = []

    def setTable(self, tag='//tr'):
        self.set_tag(tag)
        self.getHeader()
        self.getRows()

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

    def getRows(self):

        # fills remaining rows
        num = int(len(self.row_data)/2)
        for r in range(1, num): #
            T = self.row_data[r] # current row
            i = 0 # current column
            for t in T.iterchildren():
                data = t.text_content()
                self.table[i][1].append(data)
                i += 1



