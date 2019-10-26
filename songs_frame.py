"""Uses scrapper class to get song info and store as serialized object"""

from scrap import Scrapper
import pandas as pd
import pickle


# loading in data
def loadBest():
    songs_list = []
    for year in range(1960, 2017):
        url = ' http://billboardtop100of.com/' + str(year)+ '-2/'
        s = Scrapper(url)
        s.setTableB()
        df = s.getFrame()
        print(year,"\n", df.head() ,"\n")
        songs_list.append((df))

    # write dataframe into pickle file
    print("Final dataframe ", songs_list)
    with open("music_frame.pickle", "wb") as f:
        pickle.dump(songs_list, f)  # puts linear into file f

def create_csv():  # for website
    for year in range(1980, 2016):
        url = ' http://billboardtop100of.com/' + str(year)+ '-2/'
        s = Scrapper(url)
        s.setTableB()
        df = s.getFrame()
        df = df.set_index('RANK')
        df.to_csv(f'songs/songs{year}.csv')
        print(year)

create_csv()






