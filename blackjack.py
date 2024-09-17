import random
from idlelib.pyshell import restart_line
from itertools import repeat

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
you = []
com = []
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
score = int()
com_score = int()
while start == "y":
    print(art.logo)
    a = random.choice(cards)
    b = random.choice(cards)
    c = random.choice(cards)
    d = random.choice(cards)
    you.append(a)
    you.append(b)
    com.append(c)
    com.append(d)
    for n in you:
        score += n
    for m in com:
        com_score += m
    print(f"Your cards:{you},current score{score}")
    print(f"Computer's first card:{c}")
    another = input("Type 'y' to get another card, type 'n' to pass:").lower()
    while another == "y":
        e = random.choice(cards)
        you.append(e)
        score += e
        if score > 21:
            print(f"Your final hand:{you}, final score:{score}")
            print(f"Computer's first card:{c}")
            print("You went over. You lose 😭")
            another = "n"
            start = "n"
        else:
            print(f"Your cards:{you}, current score:{score}")
            print(f"Computer's first card:{c}")
            another = input("Type 'y' to get another card, type 'n' to pass:").lower()
    while com_score <= 17 and score <= 21:
        f = random.choice(cards)
        com_score += f
        com.append(f)
    if com_score >= 17 and com_score <=21:
        if score > com_score:
            print(f"Your final hand:{you}, final score:{score}")
            print(f"Computer's final hand:{com}, final score:{com_score}")
            print("You win 😃")
        elif com_score > score:
            print(f"Your final hand:{you}, final score:{score}")
            print(f"Computer's final hand:{com}, final score:{com_score}")
            print("You lose 😤")
    elif com_score > 21:
        print(f"Your final hand:{you}, final score:{score}")
        print(f"Computer's final hand:{com}, final score:{com_score}")
        print("Opponent went over. You win 😁")
    start = 'n'
