# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from idlelib.editor import keynames
from itertools import repeat

import art
print(art.logo)
bidding = {}
name = input("What is your name?:")
bidding[name] = int(input("What is your bid:?"))
repeat = input("Are there any other bidders? Type 'yes or 'no'").lower()
while repeat == "yes":
    print("\n"*20)
    name = input("What is your name?:")
    bidding[name] = int(input("What is your bid:?"))
    repeat = input("Are there any other bidders? Type 'yes or 'no'").lower()
#print(value for value,key in bidding.items() if key == max(bidding.values()))
winner = max(bidding, key=bidding.get)
print(f"Winner is : {winner}")
