import random
import os
from guessLogic import setGameMode, setGuesses

# Clear screen
os.system('cls')

# Introduction to game
print('Welcome to the Guess Game\n')
print('The object of the game is to guess the number correctly. Remember, the number will be between 1 and 100.\n')

# Pick the number for the user to guess
game_number = random.randrange(101)

# Set Game Mode
gameMode = setGameMode()
guesses = setGuesses(gameMode)

# Start of game
os.system('cls')
print(f'You\'ve selected {gameMode.title()}. Let\'s begin.\n')
# Set point to exit game loop if player guesses correctly
win = False
# Game loop
while guesses > 0 and win == False:
    # Testing Purposes
    #print(game_number)
    #print(guesses)
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