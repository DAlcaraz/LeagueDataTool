from unicodedata import name
import pandas as pd
import requests
import json 

pd.set_option("display.max_rows", None, "display.max_columns", 8)
pd.set_option('display.expand_frame_repr', False)

nameFile = open(r'C:\Users\mda03\OneDrive\Documents\Data\nameList.txt', 'r')
nameList = nameFile.read().splitlines()

for x in nameList:
    url = 'https://ddragon.leagueoflegends.com/cdn/12.9.1/data/en_US/champion/' + x + '.json'
    response = requests.get(url)
    responseText = response.text
    y = json.loads(responseText)
    print(y['data'][x]['title'])