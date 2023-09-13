# Day 4 - 100 Days of Code by Angela Yu - Udemy
## This is Day 4 project on the course. It is a Rock, Paper and Scissors game.

## The rules
### Rock wins against scissors.  0 wins 2
### Scissors wins against paper. 2 wins 1
### Paper wins against rock.     1 wins 0

## The user has to choose one of the options against the machine random choice.

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

#Write your code below this line 👇
import random
#creating a list of the possible choices
choices = [rock, paper, scissors]

#asking the user to choose 
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
while user_choice < 0 or user_choice > 2:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#creating a choice for the machine 
machine_choice = random.randint(0, 2)

#the variables of the choices
you = choices[user_choice]
machine = choices[machine_choice]

#printing the choices
print("You have chosen.\n" + you)
print("Machine has chosen.\n" + machine)

#verifying who's the winner or if it's a draw
if you != machine:
    if you == choices[0]:
        if machine != choices[2]:
            print("You loose!")
        else:
            print("You win!")
    elif you == choices[1]:
        if machine != choices[0]:
            print("You loose!")
        else:
            print("You win!")
    elif you == choices[2]:
        if machine != choices[1]:
            print("You loose!")
        else:
            print("You win!")
else:
    print("It's a draw!")    
