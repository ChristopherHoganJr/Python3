#!/usr/bin/env python3

import random

print('-------- LET THE ROCK, PAPER, SCISSORS TOURNAMENT BEGIN! --------')
print('-----------------------------------------------------------------')
print('-------- Welcome mighty warrior! We\'ve been expecting you.-------')
print(' We have 3 weapons to fight with today: Rock, Paper, or Scissors.')


def getUserChoice():
    userChoice = input('Choose your weapon warrior!\n')
    userChoice = userChoice.lower()
    if userChoice == 'rock' or userChoice == 'paper' or userChoice == 'scissors':
        print('Excellent choice! the ' + userChoice + ' is a fine weapon!')
    else:
        print('No other weapons are allowed here.')
        getUserChoice()
    return userChoice
# Assigning user's choice to a variable
weaponChoice = getUserChoice()

def getComputerChoice():
    computerChoice = random.randint(0,3)
    if computerChoice == 0:
        return 'rock'
    elif computerChoice == 1:
        return 'paper'
    else:
        return 'scissors'
# Assigning computer's choice to a variable
opponentChoice = getComputerChoice()

def playGame(userChoice, computerChoice):
    print('------ The weapons have been chosen, let the battle begin! ------')
    # Outcome if tie game
    if userChoice == computerChoice:
        print('Although the battle was fierce, no victor has been decided. DRAW!')
    # Outcome if user chose rock
    elif userChoice == 'rock':
        if computerChoice == 'scissors':
            print('You are the champion of the world! Congratulations on your victory!')
        else:
            print('You have been defeated. There were no smiles today, only tears.')
    # Outcome if user chose paper
    elif userChoice == 'paper':
        if computerChoice == 'rock':
            print('You are the champion of the world! Congratulations on your victory!')
        else:
            print('You have been defeated. There were no smiles today, only tears.')
    # Outcome if the user chose scissors
    else:
        if computerChoice == 'paper':
            print('You are the champion of the world! Congratulations on your victory!')
        else:
            print('You have been defeated. There were no smiles today, only tears.')

# Play Game
playGame(weaponChoice, opponentChoice)