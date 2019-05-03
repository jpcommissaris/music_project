from scrap import Scrapper
import pandas as pd
import pickle

songs_list = [("best", []), ("pop", []), ("rap", []), ("rock", [])]   # genre, and list of years

# loading in data
def loadBest():
    global songs_list
    for year in range(1960, 2017):
        url = ' http://billboardtop100of.com/' + str(year)+ '-2/'
        tag = '//tr'
        s = Scrapper(url)
        s.setTableB()
        df = s.getFrame()
        print(year,"\n", df.head() ,"\n")
        songs_list[0][1].append((df))

def loadPop():
    global songs_list


# extract data
loadBest()


# write dataframe into pickle file
print("Final dataframe ",songs_list[0][1])
with open("music_frame.pickle", "wb") as f:
    pickle.dump(songs_list, f)  # puts linear into file f

