# Import necessary modules and libraries
from art import logo, vs
from game_data import data
from random import randint
from replit import clear

# Initialize game variables
game_on = True
score = 0

# Main game loop
while game_on:
    # Display game logo

    print(logo)

    # Display current score if the score is greater than 0
    if score > 0:
        print(f"You're right! Current score: {score}\n")

    # Choose random indices for two data items (celebrities)
    number_1 = randint(0, len(data) - 1)
    number_2 = randint(0, len(data) - 1)

    # Ensure that number_1 and number_2 are different
    if number_1 == number_2:
        number_2 = (number_1 + 1) % len(data)

    # Display the two data items for comparison
    print(f"Compare A: {data[number_1]['name']}, a {data[number_1]['description']}, from {data[number_1]['country']}\n")
    print(vs)
    print(f"Compare B: {data[number_2]['name']}, a {data[number_2]['description']}, from {data[number_2]['country']}\n")

    # Prompt the user for their choice
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen for the next round
    clear()

    # Compare the follower counts and update the score
    if choice == 'a' and data[number_1]['follower_count'] >= data[number_2]['follower_count']:
        score += 1
    elif choice == 'b' and data[number_2]['follower_count'] >= data[number_1]['follower_count']:
        score += 1
    else:
        # End the game if the user's choice is wrong
        game_on = False
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
