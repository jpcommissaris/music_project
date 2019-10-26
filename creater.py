"""Holds the main method and args"""
from playlist import Playlist
import sys


# -- usage --
if len(sys.argv) == 1:
    print('Usage: python creator.py YEAR SLICE WEIGHT ARTIST1 ARTIST2 ....\n')
    exit(0)

if sys.argv[1] == '-h':
    w = ' WEIGHT (0-10) determines the likelihood of picking songs from a given playlist negative weight returns only songs from artists'
    s = 'SLICE adds more years to your list, 2000 with slice=10 gives songs from 2000-2010.'
    a = 'ARTISTS takes in an array of artist who you want prioritized on your playlist.'
    print(w, '\n', s,'\n', a, '\n')
    exit(0)

# default values
weight = 1
slice = 1
artists = []
year = int(sys.argv[1])


# -- get command line args --
if len(sys.argv) >= 3:
    slice = int(sys.argv[2])
if len(sys.argv) >= 4:
    weight = float(sys.argv[3])
if len(sys.argv) >= 5:
    for x in range(4, len(sys.argv)):
        artists.append(sys.argv[x])

print(f'Args: [yr={year}, slice={slice}, weight={weight}, artists={artists}] \n')


# -- create playlist --
ex = Playlist()
ex.addArg(year, weight=weight, slice=slice, artists=artists)
ex.createPlaylist()
ex.printPlaylist()





'''
Multi-arg playlist example

b = Playlist()
b.addArg(1995, slice=15, weight=-1, artists=["Kanye West"])
b.addArg(1970, slice=30, weight=-1, artists=["Michael Jackson"])
b.addArg(2010, slice=2, weight=.5)
b.createPlaylist()
b.printPlaylist()

'''