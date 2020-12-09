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



# Create playing deck
playing_deck = createDeck()
print(playing_deck)
# Initiate player 1's hand
player1_hand = []
# Initiate dealer's(computer's) hand
dealer_hand = []

def dealCard(deck=playing_deck):
    card = random.choice(deck)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def play_game():
    # Get users name
    player_1 = input('What is your name: ')
    print(f'Hello, {player_1}, welcome to blackjack!')
    print('##########################################')
    # Start game
    for i in range(2):
        player1_hand.append(dealCard())
        dealer_hand.append(dealCard())
    print(player1_hand)






play_game()
    


