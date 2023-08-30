# Import necessary modules and functions from other files
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear
import random

# Choose a random word from the list of words
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Print the game logo
print(logo)

# Initialize the display with underscores for each letter in the chosen word
display = []
for _ in range(word_length):
    display += "_"

# Main game loop
while not end_of_game:
    # Get user's letter guess, convert to lowercase
    guess = input("Guess a letter: ").lower()

    # Clear the console screen
    clear()

    # Check if the guessed letter has already been guessed before
    if guess in display:
        print("You've already guessed this letter")

    # Iterate through the letters in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        # If the guessed letter matches a letter in the word, reveal it in the display
        if letter == guess:
            display[position] = letter

    # Check if the guessed letter is not in the chosen word
    if guess not in chosen_word:
        print("That's not in the word. You lose a life.")
        lives -= 1
    # Check if the player has run out of lives
    if lives == 0:
        end_of_game = True
        print("You lose.")

    # Print the current state of the word display
    print(f"{' '.join(display)}")

    # Check if all letters have been guessed and the word is complete
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print the hangman ASCII art corresponding to the remaining lives
    print(stages[lives])