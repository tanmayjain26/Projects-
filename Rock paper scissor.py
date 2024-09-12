rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
design = [rock, paper, scissors]
computer_chose = random.choice(design)
choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
if choose == "0":
    print(rock)
    if computer_chose == scissors:
        print("Computer chose",scissors)
        print("you win")
    if computer_chose == rock:
        print("Computer chose", rock)
        print("Draw")
    else:
        print("Computer chose", paper)
        print("you lose")
elif choose == "1":
    print(paper)
    if computer_chose == rock:
        print("Computer chose",rock)
        print("you win")
    if computer_chose == paper:
        print("Computer chose", paper)
        print("Draw")
    else:
        print("Computer chose", scissors)
        print("you lose")
elif choose == "2":
    print(scissors)
    if computer_chose == paper:
        print("Computer chose",paper)
        print("you win")
    if computer_chose == scissors:
        print("Computer chose", scissors)
        print("Draw")
    else:
        print("Computer chose", rock)
        print("you lose")
else:
    print("invalid chose")