# Import the logo from the 'art' library
from art import logo
# Import the randint function from the 'random' library
from random import randint

# Print the game logo
print(logo)
# Print a welcome message
print("Welcome to the Guessing Game!\n")
# Print a message about the number range
print("I'm thinking of a number between 1 and 100\n")

# Set the initial number of attempts to 5
attempts = 5
# Generate a random number between 1 and 100
number = randint(1, 100)

# Ask the player to choose a difficulty level
decision = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# If the player chooses 'easy', increase the number of attempts to 10
if decision == "easy":
    attempts = 10

# Main game loop
while attempts != 0:
    # Display the number of remaining attempts
    print(f"\nYou have {attempts} attempts remaining to guess the number.\n")

    # Get the player's guess as an integer
    guess = int(input("Make a guess: "))

    # Check if the guess is too high, too low, or correct
    if guess > number:
        print("\nToo high.")
    elif guess < number:
        print("\nToo low.")
    else:
        print(f"\nYou got it! The answer was {number}")
        break  # Exit the loop if the guess is correct

    # Decrement the number of remaining attempts
    attempts -= 1

    # Check if the player has run out of attempts
    if attempts == 0:
        print("\nYou've run out of guesses, you lose.")
    else:
        print("\nGuess again")
