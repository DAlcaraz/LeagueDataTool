#Daniel Alcaraz
import json
import requests
import csv

file = open('leagueData.csv', 'w', newline='')
nameFile = open('nameList.txt', 'a')
writer = csv.writer(file)
response = requests.get("https://ddragon.leagueoflegends.com/cdn/13.1.1/data/en_US/champion.json")

x = response.text
y = json.loads(x)

header =      ['Name',
               'ID',
               'HP',
               'HP per level',
               'Mana',
               'Mana per level',
               'Movement speed',
               'Armor',
               'Armor per level',
               'MR',
               'MR per level',
               'Range',
               'Range type',
               'HP regen',
               'HP regen per level',
               'Mana regen',
               'Mana regen per level',
               'AD',
               'AD per level',
               'Attack speed']
writer.writerow(header)
loop = 1
problemChild = []
rangeType = ''

nameFile.truncate(0)

for x in y['data']:
        if y['data'][x]['stats']['attackrange'] > 200:
                rangeType = "Ranged"
        else:
                rangeType = "Melee"

                
        data = [
        str(y['data'][x]['name']),
        loop,
        str(y['data'][x]['stats']['hp']),
        str(y['data'][x]['stats']['hpperlevel']),
        str(y['data'][x]['stats']['mp']),
        str(y['data'][x]['stats']['mpperlevel']),
        str(y['data'][x]['stats']['movespeed']),
        str(y['data'][x]['stats']['armor']),
        str(y['data'][x]['stats']['armorperlevel']),
        str(y['data'][x]['stats']['spellblock']),
        str(y['data'][x]['stats']['spellblockperlevel']),
        str(y['data'][x]['stats']['attackrange']),
        rangeType,
        str(y['data'][x]['stats']['hpregen']),
        str(y['data'][x]['stats']['hpregenperlevel']),
        str(y['data'][x]['stats']['mpregen']),
        str(y['data'][x]['stats']['mpregenperlevel']),
        str(y['data'][x]['stats']['attackdamage']),
        str(y['data'][x]['stats']['attackdamageperlevel']),
        str(y['data'][x]['stats']['attackspeed'])
        ]

        #Wukong is a problem child because his reference name is 'Monkey King' 
        #so he's out of alphabetical order
        #Manually put him in front of Xayah:
        
        if str(y['data'][x]['name']) == 'Wukong':
                problemChild = data
                problemChild[1] = 145

        elif str(y['data'][x]['name']) == 'Xayah':
                writer.writerow(problemChild)
                nameFile.write("Wukong" + '\n')
                data[1] = 146
                nameFile.write("Xayah" + '\n')
                writer.writerow(data)
                loop = loop + 2
        else:         
                loop = loop + 1
                nameFile.write(data[0].replace(' ', '').replace('.', '').replace("'", '') + '\n')
                writer.writerow(data)
file.close()
print('done')