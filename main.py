import os
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bidders_data = []
bid_available = True
highest_bidder = ''
highest_bid = 0

while bid_available:
    bidders_name = input("What is your name: ").lower()
    bid_amount = int(input("What's your bid: $"))
    bidders_data.append({'name': bidders_name, 'amount': bid_amount})
    clear_screen = input("Are there any other bidders : ").lower()

    if clear_screen == 'yes':
        os.system('cls')
    elif clear_screen == 'no':
        os.system('cls')
        bid_available = False
        for bidder in bidders_data:
            if bidder['amount'] > highest_bid:
                highest_bidder = bidder['name']
                highest_bid = bidder['amount']
        print(f"The Highest bid is {highest_bid} by {highest_bidder}")
    else:
        os.system('cls')
        print("Invalid Input")
        exit()

