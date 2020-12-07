import os
from auctionArt import logo
from silentAlgorithm import find_highest_bidder

print(logo)

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input('What is your name?: ')
    price = int(input('What is your bid?: $'))
    bids[name] = price
    should_continue = input('Are there any other bidders? Type \'yes\' or \'no\'.\n').lower()
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        os.system('cls')