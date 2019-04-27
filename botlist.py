import pickle
import pandas
import random


class Playlist:
    def __init__(self):
        # read in model with pickle
        pickle_in = open("musics_frame.pickle", "rb")
        self.table = pickle.load(pickle_in)
        # data
        self.args = []
        self.songs = []

    def addArg(self, genre, year, weight=1.0):
        self.args.append((genre,year,weight))

    def createPlaylist(self):
        for arg in self.args:
            genre = self.getGenre(arg[0])  # genre by number
            year = arg[1]-1970
            weight = arg[2]
            frame = self.table[genre][1][year]
            for index, row in frame.iterrows():
                self.addSong(index+1, row[1], row[2], weight)
    def printPlaylist(self):
        for song in self.songs:
            print(song)

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

    def addSong(self, rank, artist, song, weight):
        chance = int(self.prob(rank, weight))
        rand = random.randint(0,99)
        print(chance, rand)
        if chance > rand:
            self.songs.append(" - "+ song + ", by: " + artist)

    def prob(self, rank, w):
        if rank == 1:
            return 90 * w
        elif 1 < rank <=5:
            return 80 * w
        elif 5 <= rank <= 12:
            return 60 * w
        elif 12 < rank <= 20:
            return 50 * w
        elif 20 < rank <= 35:
            return 35 * w
        elif 35 < rank:
            return 25 * w
        return 0

# test
b = Playlist()
b.addArg("best", 2000, weight=1.1)
b.createPlaylist()
b.printPlaylist()



