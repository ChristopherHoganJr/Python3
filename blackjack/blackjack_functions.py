import random

def createDeck():
    playing_cards = []
    for i in range(52):
        if i % 13 + 1 > 10:
            playing_cards.append(10)
        elif i % 13 + 1 == 1:
            playing_cards.append(11)
        else:
            playing_cards.append(i % 13 + 1)
    return playing_cards

def dealCard(deck):
    card = random.choice(deck)
    return card

def calculate_score(cards):
    # Take a list of cards and return the score of the cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Draw.'
    elif computer_score == 0 and user_score == 0:
        return 'DOUBLE BLACKJACK!!!!'
    elif computer_score == 0:
        return 'Lose, computer has a blackjack.'
    elif user_score == 0:
        return 'Win! You have a blackjack.'
    elif user_score > 21:
        return 'Lose, you went over 21.'
    elif computer_score > 21:
        return 'Win! Computer went over 21.'
    elif user_score > computer_score:
        return 'Win!'
    else:
        return 'You Lose.'