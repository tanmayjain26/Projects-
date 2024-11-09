from game_data import data
from art import logo
from art import vs
import random
print(logo)
score =0
game = True
b = random .choice(data)
while game:
    a = b
    b = random.choice(data)
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.")
    print(vs)
    print(f"Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.")
    guess = input("Who has more followers? Type 'A' or 'B':").lower()
    if guess == "a":
        if a["follower_count"] > b["follower_count"]:
            score += 1
            print(" \n" * 20)
            print(logo)
            print("You're right! Current score:",score)
        else:
            print("Sorry, that's wrong. Final score:",score)
            game = False
    elif guess == "b":
        if b["follower_count"] > a["follower_count"]:
            score+=1
            print(" \n" * 20)
            print(logo)
            print("You're right! Current score:",score)
        else:
            print("Sorry, that's wrong. Final score:",score)
            game = False
    else:
        print("Sorry, that's wrong. Final score:", score)
        game = False
