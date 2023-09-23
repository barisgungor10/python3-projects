### It is working well but only thing is not working is sometimes game gives same names to user ( i think pop does not work ) 

# Import necessary modules and libraries
from art import logo, vs
from game_data import data
from random import randint
from replit import clear

# Initialize game variables
game_on = True  # Flag to control the game loop
score = 0  # Initialize the player's score

# Choose random indices for two data items (celebrities)
number_1 = randint(0, len(data) - 1)
number_2 = randint(0, len(data) - 1)

# Main game loop
while game_on:
    # Display game logo
    print(logo)

    # Display current score if the score is greater than 0
    if score > 0:
        print(f"You're right! Current score: {score}\n")

    # Display the two data items for comparison
    print(
        f"Compare A: {data[number_1]['name']}, a {data[number_1]['description']}, from {data[number_1]['country']}\n"
    )
    print(vs)
    print(
        f"Compare B: {data[number_2]['name']}, a {data[number_2]['description']}, from {data[number_2]['country']}\n"
    )

    # Prompt the user for their choice
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen for the next round
    clear()

    # Compare the follower counts and update the score
    if choice == 'a' and data[number_1]['follower_count'] >= data[number_2]['follower_count']:
        # Remove the data item that was not chosen for the next round
        data.pop(number_2)
        # Generate a new random index for the remaining data
        number_2 = randint(0, len(data) - 1)
        score += 1
    elif choice == 'b' and data[number_2]['follower_count'] >= data[number_1]['follower_count']:
        # Remove the data item that was not chosen for the next round
        data.pop(number_1)
        # Update the indices for the remaining data
        number_1 = number_2
        number_2 = randint(0, len(data) - 1)
        score += 1
    else:
        # End the game if the user's choice is wrong
        game_on = False
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
