import pickle
import pandas
import random


class Playlist:
    def __init__(self):
        # read in model with pickle
        pickle_in = open("music_frame.pickle", "rb")
        self.table = pickle.load(pickle_in)
        # data
        self.args = []
        self.songs = []

    def addArg(self, genre, year, weight=1.0, slice=1, artists=[]):
            for x in range(0,slice):
                self.args.append((genre, year+x, weight*(1/slice), artists))

    def createPlaylist(self):
        for arg in self.args:
            genre = self.getGenre(arg[0])  # genre by number
            year = arg[1]-1960
            frame = self.table[genre][1][year]
            for index, row in frame.iterrows():
                self.addSong(index+1, row[1], row[2], arg[2], arg[3])

    def printPlaylist(self):
        #random.shuffle(self.songs)
        i=1
        print("Your playlist: ")
        for song in self.songs:
            print(song)
            if i % 5 == 0:
                print("")
            i+=1
        print("\n")

    # helper methods
    def getGenre(self, g):
        if g == "best":
            return 0
        elif g == "pop":
            return 1
        elif g == "rap":
            return 2
        elif g == "rock":
            return 3

    def addSong(self, rank, artist, song, weight, artists):
        chance = int(self.prob(rank, artist, weight, artists))
        rand = random.randint(0,99)
        dup = self.checkDup(artist, song)
        top5 = ""
        if rank <= 5:
            top5 = "(top 5)"
        if chance > rand and not dup:
            self.songs.append(" - " + song + ",  by: " + artist + " " + top5 )

    def prob(self, rank, a, w, artists):
        for people in artists:
            if people in a:
                return 100
        if not w < 0:
            if 0 < rank <= 3:
                return 100
            elif 3 < rank <= 6:
                return 85 * (w+.1)
            elif 6 < rank <= 12:
                return 60 * w
            elif 12 < rank <= 20:
                return 40 * w
            elif 20 < rank <= 40:
                return 25 * w
            elif 40 < rank:
                return 15 * w
        return 0

    def checkDup(self, artist, song):
        for x in self.songs:
            if " - " + song + ",  by: " + artist in x:
                return True
        return False


# test
'''b = Playlist()
b.addArg("best", 2005, weight=.5)
b.addArg("best", 2006, weight=.5)
b.addArg("best", 2007, weight=.5)
b.createPlaylist()
b.printPlaylist()'''



