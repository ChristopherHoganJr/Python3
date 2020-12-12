import random
import os
from guessLogic import logo, setGameMode, setGuesses

# Clear screen
os.system('cls')

# Introduction to game
print(logo)
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

# Initiate hints for player
lowMin = 0
highMax = 100
# Game loop
while guesses > 0 and win == False:
    # Game Logic
    print(f'The number is between {lowMin} and {highMax}\n')
    print(f'Available Guesses: {guesses}')
    user_guess = int(input('What is your guess?: '))
    if user_guess > game_number:
        guesses -= 1
        os.system('cls')
        print(f'{user_guess} is too high.\n')
        highMax = user_guess
    elif user_guess < game_number:
        guesses -= 1
        os.system('cls')
        print(f'{user_guess} is too low.\n')
        lowMin = user_guess
    else:
        win = True

# Player has ran out of guesses and lost the game
if guesses == 0:
    print('Sorry, you ran out of guesses. You lose.')
# Player has guessed correctly and won the game
if win == True:
    os.system('cls')
    print(f'You did it! You guessed {game_number} correctly! You win!')
    print(f'Guesses left: {guesses}')