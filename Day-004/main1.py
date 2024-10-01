# 100 Days of Python - Day 004
# Ex05: Rock-Paper-Scissors Game Project

import random
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

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

choices = [rock, paper, scissors]

computer_choice = choices[random.randint(0, 2)]
player_choose = choices[player_choice]

def game():
    if player_choose == rock and computer_choice == scissors or player_choose == scissors and computer_choice == paper or player_choose == paper and computer_choice == rock:
        return f"Computer Choose:\n{computer_choice}\nYour Choice:\n{player_choose}\nYou Win!"
    elif player_choose == computer_choice:
        return f"Computer Choose:{computer_choice}\nYour Choice:\n{player_choose}\nIt's a Draw!"
    else:
        return f"Computer Choose:{computer_choice}\nYour Choice:\n{player_choose}\nYou Loose!"

print(game())