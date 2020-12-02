import random
import datetime

todaysDate = datetime.date.today()

computer_opponents = ['Sophia', 'Liam', 'Olivia', 'Noah', 'Riley', 'Jackson', 'Emma', 'Aiden']

print('--- Welcome to the Rock, Paper, Scissors Tournament ---')
# Picking Player Names
players_string = input('Who is competing today?\n')
players_list = players_string.split(', ')
player1 = players_list[0]
players_list.append(computer_opponents[random.randint(0, len(computer_opponents)-1)])
player2 = players_list[1]
print(f'We have an exciting match today, {todaysDate}. {player1} is in the left corner and {player2} in the right corner')

# Weapons to choose from
weapon_choice = ['rock','paper','scisscors']

# Player 1 picking weapon
def player1weapon():
    player1_weapon = input(f'{player1.upper()} CHOOSE YOUR WEAPON!: \'ROCK\', \'PAPER\', \'SCISSORS\'\n')
    player1_choice = player1_weapon.lower()
    if player1_choice not in weapon_choice:
        player1weapon()
    return player1_choice

player1_weapon = player1weapon()

# Computer picking weapon
player2_weapon = weapon_choice[random.randint(0, 2)]

# Battle stage
print('LET THE BATTLE BEGIN!!! PLAYERS HAVE LOCKED IN THIER WEAPON OF CHOICE')
def battleStage(player1_weapon, player2_weapon):
    if player1_weapon == 'rock':
        if player2_weapon == 'rock':
            outcome = 2
            return outcome
        elif player2_weapon == 'paper':
            outcome = 1
            return outcome
        else:
            outcome = 0
            return outcome
    elif player1_weapon == 'paper':
        if player2_weapon == 'rock':
            outcome = 0
            return outcome
        elif player2_weapon == 'paper':
            outcome = 2
            return outcome
        else:
            outcome = 1
            return outcome
    else:
        if player2_weapon == 'rock':
            outcome = 1
            return outcome
        elif player2_weapon == 'paper':
            outcome = 0
            return outcome
        else:
            outcome = 2
            return outcome
    return outcome

winner = battleStage(player1_weapon, player2_weapon)
# Annouce the winner
if winner < 2:
    print(f'It was a challanging battle. Both players tried their best with their weapon.\nBut as we know, there can only be one winner. Today, we crown {players_list[winner]} the winner')
else:
    print('They killed each other. Game over.')

print(player2_weapon)



