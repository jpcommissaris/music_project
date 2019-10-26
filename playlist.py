"""Creates a playlist from songs"""
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

    def addArg(self, year, weight=1.0, slice=1, artists=[]):
            for x in range(0,slice):
                self.args.append((year+x, weight*(1/slice), artists))

    def createPlaylist(self):
        for arg in self.args:
            year = int(arg[0]-1960)
            frame = self.table[year]
            for index, row in frame.iterrows():
                self.addSong(index+1, row[1], row[2], arg[1], arg[2])

    # -- prints the final playlist to the console --
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


    # -- adds a song to the playlist --
    def addSong(self, rank, artist, song, weight, artists):
        chance = int(self.prob(rank, artist, weight, artists))
        rand = random.randint(0,99)
        dup = self.checkDup(artist, song)
        top5 = ""
        if rank <= 5:
            top5 = "(top 5)"
        if chance > rand and not dup:
            self.songs.append(" - " + song + ",  by: " + artist + " " + top5 )

    # -- calculates the odds a song will appear in a playlist --
    def prob(self, rank, a, w, artists):
        w = w/4
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

    # -- ensures no playlist has duplicate songs --
    def checkDup(self, artist, song):
        for x in self.songs:
            if " - " + song + ",  by: " + artist in x:
                return True
        return False





