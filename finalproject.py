import random
import time
import math
rosternum = 0
roster = []
totalppg = 0
totalapg = 0
totalrpg = 0
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

player_stats = {}
for name, ppg, apg, rpg in starmatch + stripematch + worldmatch:
    player_stats[name] = {"ppg": ppg, "apg": apg, "rpg": rpg}




def predict_season_record(totalppg, totalapg, totalrpg):
    rating = totalppg * 1.0 + totalapg * 1.5 + totalrpg * 1.3
    wins = round((rating - 140) * 0.45 + 50)
    wins = max(40, min(82, wins))
    losses = 82 - wins
    return wins, losses


def pick_player(team_choice):
    if team_choice.lower() == "usa stripes":
        return random.choice(usastripes['Names'])
    elif team_choice.lower() == "usa stars":
        return random.choice(usastars['Names'])
    elif team_choice.lower() == "world players":
        return random.choice(worldplayers['Names'])
    else:
        return None

print("nba all-star 82-0 game")
time.sleep(1)
print("you'll be given a random player from a random team from the 2025-2026 nba all-star roster")
time.sleep(2)
print("your goal is to pick 5 and see how they do")
time.sleep(2)
team = input("first, pick a team, usa stars, usa stripes, and world players: ")
print("you chose", team)
time.sleep(1)
print("next you'll get a random player from the team")
player = pick_player(team)
if player is None:
    print("not a team")
    raise SystemExit

time.sleep(3)
print("you got", player)
roster.append(player)
stats = player_stats[player]
totalppg += stats['ppg']
totalapg += stats['apg']
totalrpg += stats['rpg']
rosternum += 1
while rosternum < 5:
    try:
        team2 = input("now pick another team (usa stars, usa stripes, and world players): ")
        player = pick_player(team2)
        if player is None:
            print("not a team")
            break
        time.sleep(3)
        print("you got", player)
        roster.append(player)
        stats = player_stats[player]
        totalppg += stats['ppg']
        totalapg += stats['apg']
        totalrpg += stats['rpg']

        rosternum += 1
    except ValueError:
        break
if rosternum == 5:
    time.sleep(1)
    print("now that you've gotten 5 players, your roster is")
    print(roster)
    print("total ppg:", round(totalppg, 1))
    print("total apg:", round(totalapg, 1))
    print("total rpg:", round(totalrpg, 1))
    wins, losses = predict_season_record(totalppg, totalapg, totalrpg)
    print(f"the predicted regular season win record of this team is {wins}-{losses}")



