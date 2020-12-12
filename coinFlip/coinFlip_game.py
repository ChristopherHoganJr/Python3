import random
import json

player_name = input('What is your name?: ').lower()
player_choice = input('Do you pick heads or tails?: ').lower()

coin_flip = random.randint(0,1)

with open('coinFlip_data.json', 'r') as player_data:
    data = json.load(player_data)

if coin_flip == 0 and player_choice == 'heads':
    data[player_name]['wins'] += 1
else:
    data[player_name]['losses'] += 1

with open('coinFlip_data.json', 'w') as player_data:
    json.dump(data,player_data)





