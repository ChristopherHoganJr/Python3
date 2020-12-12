import random
import os

os.system('cls')
# Pick the number for the user to guess
game_number = random.randrange(101)

# Initiate guesses
gameMode = input('Which mode would you like to play?\n\'Easy\' or \'Hard\': ').lower()
if gameMode == 'easy':
    guesses = 10
elif gameMode == 'hard':
    guesses = 5

# Start of game
print(f'You\'ve selected {gameMode.title()}. Let\'s begin.')
# Set point to exit game loop if player guesses correctly
win = False
# Game loop
while guesses > 0 and win == False:
    # Testing Purposes
    print(game_number)
    print(guesses)
    # Game Logic
    user_guess = int(input('What is your guess?: '))
    if user_guess > game_number:
        guesses -= 1
        print(f'{user_guess} is too high.')
    elif user_guess < game_number:
        guesses -= 1
        print(f'{user_guess} is too low.')
    else:
        win = True

# Player has ran out of guesses and lost the game
if guesses == 0:
    print('Sorry, you ran out of guesses. You lose.')
# Player has guessed correctly and won the game
if win == True:
    os.system('cls')
    print(f'You did it! You guessed the {game_number} correctly! You win!')