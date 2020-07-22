#!/usr/bin/env python

import random

userName = input('What is your name?\n')
print('It\'s great to see you ' + userName + '!')
userQuestion = input('What question do you have about your future?\n')
print('Hmmm.. okay, so you want to know... ' + userQuestion)

answer = random.randint(0,7)

if answer == 0:
    eightBall = 'It is certain'
elif answer == 1:
    eightBall = 'It is decidedly so'
elif answer == 2:
    eightBall = 'Reply hazy try again'
elif answer == 3:
    eightBall = 'Cannot predict now'
elif answer == 4:
    eightBall = 'Do not count on it'
elif answer == 5:
    eightBall = 'My sources say no'
elif answer == 6:
    eightBall = 'Outlook not so good'
elif answer == 7:
    eightBall = 'Signs point to yes'

print(eightBall)