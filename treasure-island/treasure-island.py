# Printing the ASCII art title
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

# Printing the game introduction
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# Getting user input for the first decision
condition_1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" \n').lower()

# Checking the first decision
if condition_1 == "left":
    # Getting user input for the second decision
    condition_2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()

    # Checking the second decision
    if condition_2 == "wait":
        # Getting user input for the third decision
        condition_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? \n").lower()

        # Checking the third decision
        if condition_3 == "red":
            # Player chose the red door
            print("Burned by fire.")
            print("Game Over.")
        elif condition_3 == "blue":
            # Player chose the blue door
            print("Eaten by beasts.")
            print("Game Over.")
        elif condition_3 == "yellow":
            # Player chose the yellow door
            print("You win!")
        else:
            # Player chose an invalid option
            print("Game Over.")

    else:
        # Player chose to swim across the lake
        print("Attacked by trout.")
        print("Game Over")

else:
    # Player chose to go right at the crossroad
    print("Fall into a hole.")
    print("Game Over")