import os
from blackjack_art import logo
from blackjack_functions import createDeck, dealCard, calculate_score, compare

def play_game():
    # Initiating start of game
    os.system('cls')
    playing_deck = createDeck()
    user_cards = []
    computer_cards = []
    players_turn = True
    computers_turn = False

    print(logo)
    print('Welcome to Python Blackjack')
    # Deals 2 cards to players
    for _ in range(2):
        user_cards.append(dealCard(playing_deck))
        computer_cards.append(dealCard(playing_deck))


    while players_turn:
        # Adds up the score of players
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'    Your cards: {user_cards}, current score: {user_score}')
        print(f'    Computer\'s first card: {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            players_turn = False
        else:
            user_should_deal = input('Type \'y\' to get another card, type \'n\' to pass: ')
            if user_should_deal == 'y':
                user_cards.append(dealCard(playing_deck))
            else:
                players_turn = False
                computers_turn = True

    while computers_turn:
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(dealCard(playing_deck))
            computer_score = calculate_score(computer_cards)
        computers_turn = False

    print(f'Your cards: {user_cards}')
    print(f'Computer\'s cards: {computer_cards}')
    print(compare(user_score,computer_score))

    play_again = input('Do you want to play another game of Blackjack? Type \'yes\' or \'no\': ').lower()
    if play_again == 'yes' or play_again == 'y':
        os.system('cls')
        play_game()
    
play_game()