from botlist import Playlist

# -- Simple playlist creator that takes popular songs from billboards.com and compiles them into a playlist --
# genre can be best, pop, rap or rock
# year must be a number between 1970 and 2017
# weight determines the likelihood of picking songs from a given playlist
# 0 weight give top 3, 10 weight gives you everything, negative weight returns only songs from the artists chosen
# slice adds more years to your list, 2000 with slice=10 gives songs from 2000-2010
# artists takes in an array of artist who you want prioritized on your playlist
# add more arguments to change up the playlist


# example
ex = Playlist()
ex.addArg("best", 2000)
ex.addArg("best", 2005, weight=.5, slice=3, artists=["Drake", "LMFAO"])
ex.createPlaylist()
# ex.printPlaylist(

# create below

a = Playlist()
a.addArg("best", 1960, slice=20, weight=-1, artists=["Beatles"])
a.createPlaylist()

b = Playlist()
b.addArg("best", 1995, slice=15, weight=-1, artists=["Kanye West"])
b.createPlaylist()

c = Playlist()
c.addArg("best", 1970, slice=30, weight=-1, artists=["Michael Jackson"])
c.createPlaylist()

d = Playlist()
d.addArg("best", 2014, slice=3, weight=.5)
d.createPlaylist()

#a.printPlaylist()
b.printPlaylist()
#c.printPlaylist()
#d.printPlaylist()

 # new stuff