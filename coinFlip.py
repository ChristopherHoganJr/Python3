import random

def coinFlip():
    player1 = input('Do you pick heads or tails?\n')
    player1_choice = player1.lower()
    random_side = random.randint(0,1)
    winner = ''
    if random_side == 1:
        winner = 'heads'
    else:
        winner = 'tails'
    if winner == player1_choice:
        print(f'You win! The coin flip landed on {winner}!')
    else:
        print(f'You lose! The coin flip landed on {winner}!')
    again = input('Do you want to play again?\n')
    if again.lower() == 'yes':
        coinFlip()
    else:
        print('Have a good day!')

coinFlip()