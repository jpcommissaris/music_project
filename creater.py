from botlist import Playlist


# genre can be best, pop, rap or rock
# year must be a number between 1970 and 2017
# weight determines the likelihood of picking songs from a given playlist
# 0 weight give top 3, 10 weight gives you everything, negative weight returns only songs from the artists chosen
# slice adds more years to your list, 2000 with slice=10 gives songs from 2000-2010
# add more arguments to change up the playlist



# create
a = Playlist()
a.addArg("best", 2000, weight=1)
a.createPlaylist()

b = Playlist()
b.addArg("best", 2005, weight=.5)
b.addArg("best", 2006, weight=.5)
b.addArg("best", 2007, weight=.5)
b.createPlaylist()

c = Playlist()
c.addArg("best", 1995, slice=15, weight=-1, artists=["Kanye West"])
c.createPlaylist()


# print
c.printPlaylist()

