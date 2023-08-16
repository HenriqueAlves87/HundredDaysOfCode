# Day 3 - 100 Days of Code by Angela Yu - Udemy
# This is Day 3 project on the course. It is a Treasure Hunt.

# The user has to choose one of the options and try to get the treasure. 

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
      ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("Wich side dou you choose: left or right?\n").lower()

if choice1 == "left":
    print(f"You chose to go {choice1} and found a river.")
    choice2 = input("What do you choose: swim or wait?\n").lower()
    if choice2 == "wait":
        print(f"You chose to {choice2}, a boat appears and you made the cross safetely." + "\U0001F6F6")
        choice3 = input("You found a temple with three colored doors. Which door do you choose: red, blue or yellow?\n").lower()
        if choice3 == "red":
            print(f"You chose the {choice3} door, as you open the door a burning fire came out and burned you. Game Over." + "\U0001F975")
        elif choice3 == "yellow":
            print(f"You chose the {choice3} door, congratulations! You found the treasure!" + "\U0001F973")
        elif choice3 == "blue":
            print(f"You chose the {choice3} door, you chose the wrong door, a giant zombie came out from it and ate you. Game over." + "\U0001F9DF")
        else:
            print("You chose wrong and a giant wrecking ball fell over you. Game over.")
    elif choice2 == "swim":
        print(f"You chose to {choice2} and has been attacked by a white shark. Game over." + "\U0001F988")
    else:
        print("You chose wrong and a crocodile ate you. Game over." + "\U0001F40A")
elif choice1 == "right":
    print(f"You chose to go {choice1} and you fall into a hole. Game over." + "\U0001F635")
else:
    print("You chose wrong and the ground starts to breakdown, you fall into the hole. Game over" + "\U0001F635")
