from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f'{account_name}, a {account_descr}, from {account_country}.'

def check_answer(guess, a_followers, b_followers):
    """Use if statement to check if user is correct."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

# Display Game Art
os.system('clear')
print(logo)
score = 0
game_should_continue = True
# Make account at position B become the next account at position A
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b 
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f'Compare A: {format_data(account_a)}.')
    print(vs)
    print(f'Against B: {format_data(account_b)}.')

    # Ask the user for a guess
    guess = input('Who has more followers? A or B: ').lower()

    # Check if user is correct
    ## Get follower count for each account.
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds
    os.system('clear')
    print(logo)
    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right!\nCurrent score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, you're wrong.\nFinal score: {score}")






