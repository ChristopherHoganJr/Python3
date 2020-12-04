#!/usr/bin/env python

import random

userName = input('What is your name?\n')
print('It\'s great to see you ' + userName + '!')


def playGame():
    userQuestion = input('What question do you have about your future?\n')
    print('Hmmm.. okay, so you want to know... ' + userQuestion)
    answer = random.randint(0,7)
    if answer == 0:
        gameAnswer = 'It is certain'
    elif answer == 1:
        gameAnswer = 'It is decidedly so'
    elif answer == 2:
        gameAnswer = 'Reply hazy try again'
    elif answer == 3:
        gameAnswer = 'Cannot predict now'
    elif answer == 4:
        gameAnswer = 'Do not count on it'
    elif answer == 5:
        gameAnswer = 'My sources say no'
    elif answer == 6:
        gameAnswer = 'Outlook not so good'
    elif answer == 7:
        gameAnswer = 'Signs point to yes'
    print(gameAnswer)
    again = input('Do you have another question?\n')
    if again.lower() == 'yes':
        playGame()
    else:
        print('May your future be bright.')

playGame()