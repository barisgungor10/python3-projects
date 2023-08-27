import random

# ASCII art for the game options
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

# Store the options in a list for easier access
options_list = [rock, paper, scissors]

# Get the player's choice
p_index = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Check if the player's choice is valid
if p_index > 2 or p_index < 0:
    print("You entered an invalid number!")
else:
    print(f"Player Chooses:\n{options_list[p_index]}")

    # Generate a random choice for the computer
    c_index = random.randint(0, 2)
    print(f"Computer Chooses:\n{options_list[c_index]}")

    # Determine the winner based on the choices
    if p_index == c_index + 1 or p_index == c_index - 2:
        print("You win")
    elif c_index == p_index + 1 or c_index == p_index - 2:
        print("You Lose")
    else:
        print("It's a Draw")
        print("-")  # Separating line for clarity
