import random
import os
from hangman_words import movie_list
from hangman_art import stages, logo

# Initialize points
points = 6

# Take a random word from the word list
winning_word = random.choice(movie_list)
chosen_word = winning_word.lower()
word_length = len(chosen_word)
# Eliminate special characters that could be in list items
pass_character = ['.',' ','\'',',',':',';']

# Create an empty list of characters from word
display_list = []
# If the character in the word is a letter store it as _ else show special character
for i in range(word_length):
    if chosen_word[i] in pass_character:
        display_list.append(chosen_word[i])
    else:    
        display_list.append('_')
display = ''
for i in range(word_length):
    display += display_list[i]
# Initialize list of letter user has chosen that are not in string
not_list = []

# Start screen
os.system('cls')
print(logo)
startGame = input('Welcome to hangman!\nType \'start\' when you\'re ready\n').lower()
if startGame == 'start':
    # Clear Start Screen
    os.system('cls')
    # Show user current status of game
    print(stages[points])
    print(f'Letters that are not in movie title:\n{not_list}')
    print(f'Current word: {display}')



    end_of_game = False
    while not end_of_game:
        # Remind the player they've entered a repeated word
        repeat_word = False
        # Ask the user to guess a letter
        guess = input('Guess a letter: ').lower()

        # Check if user's letter is in the random word
        for i in range(word_length):
            if guess == display_list[i]:
                repeat_word = True
            if guess == chosen_word[i]:
                display_list[i] = guess
        if guess not in chosen_word:
            if guess in not_list:
                repeat_word = True
            else:
                points -= 1
                not_list.append(guess)

        # Convert display into a string so it looks better for user
        display = ''
        for i in range(word_length):
            display += display_list[i]

        # Clear Screen
        os.system('cls')
        # Print current status
        print(stages[points])
        print(f'Letters guessed that are not in movie title:\n{not_list}\n')
        print(f'You have {points} guesses left.')
        if repeat_word == True:
            print(f'You\'ve already guessed \'{guess}\'. Try another letter.')
        print(f'Current word: {display}')
        
        # End game loop
        if '_' not in display:
            end_of_game = True
            # Clear Screen
            os.system('cls')
            print('You Win')
            print(f'The movie was {winning_word}')
        if points == 0:
                end_of_game = True
                print('You lose')
