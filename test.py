from scrap import Scrapper
import pandas as pd

url = ' http://billboardtop100of.com/2014-2/'
tag = '//tr'
s = Scrapper(url)

s.setTable()
df = s.getFrame()
print(df)
