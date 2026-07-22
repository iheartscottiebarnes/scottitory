import random
import time

randomize = ['USA Stars', 'USA Stripes', 'World Players'
]
starstats = {
    'ppg': [18.1, 26.1, 23.9, 19.5, 28.8, 17.1, 22.5, 28.3],
    'apg': [5.9, 6, 9.9, 2, 3.7, 1.7, 7.9, 6.6],
    'rpg': [7.5, 3.9, 5.5, 10.5, 5, 8.9, 10.3, 4.1]
}
stripestats = {
    'ppg': [28.7, 26, 26, 18.6, 21.5, 20.9, 27.9, 27.9, 26.6],
    'apg': [5.1, 6.8, 4.8, 6.2, 3.7, 7.2, 3.6, 5.7, 4.7],
    'rpg': [6.9, 3.3, 5.5, 3.8, 5.6, 6.1, 6.4, 4.5, 3.6]
}
worldstats = {
    'ppg': [24.2, 33.5, 31.1, 27.7, 25.4, 21.7, 20.4, 24, 20.1, 25, 27.6],
    'apg': [6.7, 8.3, 6.6, 10.7, 7.1, 2.5, 6.2, 3.8, 3, 3.1, 5.4],
    'rpg': [6.9, 7.7, 4.3, 12.9, 4.4, 3.5, 8.9, 6.6, 11.9, 11.5, 9.8]
}
usastars = {
    "Names": ['Scottie Barnes', 'Devin Booker', 'Cade Cunningham', 'Jalen Duren', 'Anthony Edwards', 'Chet Holmgren',
    'Jalen Johnson', 'Tyrese Maxey']
}
usastripes = {
    "Names": ['Jaylen Brown', 'Jalen Brunson', 'Kevin Durant', 'DeAaron Fox',
    'Brandon Ingram', 'LeBron James', 'Kawhi Leonard', 'Donovan Mitchell', 'Stephen Curry']
}
worldplayers = {
    "Names": ['Deni Avdija', 'Luka Doncic', 'Shai Gilgeous-Alexander', 'Nikola Jokic', 'Jamal Murray', 'Norman Powell', 
    'Alperen Sengun', 'Pascal Siakam', 'Karl-Anthony Towns', 'Victor Wembanyama', 'Giannis Antetokounmpo']
}
starmatch = list(zip(usastars['Names'], starstats['ppg'], starstats['apg'], starstats['rpg']))
stripematch = list(zip(usastripes['Names'], stripestats['ppg'], stripestats['apg'], stripestats['rpg']))
worldmatch = list(zip(worldplayers['Names'], worldstats['ppg'], worldstats['apg'], worldstats['rpg']))

print("nba all-star 82-0 game")
time.sleep(1)
print("you'll be given a random player from a random team from the 2025-2026 nba all-star roster")
time.sleep(2)
print("your goal is to pick 5 and see how they do")
time.sleep(2)
print("first, spinning for a team...")
team = random.choice(randomize)
time.sleep(3)
print("you got", team)
time.sleep(3)
print("next you'll get a random player from the team")
if team.lower() == "usa stripes":
    player = random.choice(usastripes['Names'])
elif team.lower() == "usa stars":
    player = random.choice(usastars['Names'])
elif team.lower() == "world players":
    player = random.choice(worldplayers['Names'])
time.sleep(3)
print(player)


