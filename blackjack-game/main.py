############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Import necessary libraries
import random  # For generating random cards
from replit import clear  # For clearing the console
from art import logo  # For displaying the game logo

# Define a function to play the game
def play_game():
    clear()  # Clear the console
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Define the deck of cards

    # Define a function to get a random card from the deck
    def random_card():
        return random.choice(cards)

    # Define a function to calculate the sum of cards in a hand
    def sum_of_cards(cards):
        sum = 0
        for card in cards:
            sum += card
        return sum

    # Define a function to convert an Ace from 11 to 1 if needed
    def convert_ace(cards):
        for number in range(len(cards) - 1):
            if (cards[number] == 11):
                cards[number] = 1

    # Initialize player and computer hands with two random cards each
    player_cards = [random_card(), random_card()]
    computer_cards = [random_card(), random_card()]

    # Display the game logo and initial hand information
    print(logo)
    print(
        f"\n\tYour cards:{player_cards}, current score: {sum_of_cards(player_cards)}"
    )
    print(f"\tComputer's first card: {computer_cards[0]}")

    condition = True  # Initialize the game condition variable

    # Main game loop
    while condition:
        take_card = input("\nType 'y' to get another card, type 'n' to pass: ")
        if take_card == 'y':
            player_cards.append(random_card())  # Add a random card to the player's hand
            if 11 in player_cards and sum_of_cards(player_cards) > 21:
                convert_ace(player_cards)  # Convert an Ace from 11 to 1 if the player goes over 21

            # Display player's current hand and the computer's first card
            print(
                f"\n\tYour cards:{player_cards}, current score: {sum_of_cards(player_cards)}"
            )
            print(f"\tComputer's first card: {computer_cards[0]}")

            # Check if the player's score is greater than 21 (busted)
            if sum_of_cards(player_cards) > 21:
                print("\nYou went over. You lose😭\n")
                condition = False
        elif take_card == 'n':
            # Computer's turn to draw cards until its score is at least 17
            while sum_of_cards(computer_cards) < 17:
                if 11 in computer_cards and sum_of_cards(computer_cards) > 21:
                    convert_ace(computer_cards)  # Convert an Ace from 11 to 1 if the computer goes over 21
                computer_cards.append(random_card())  # Add a random card to the computer's hand

            # Display both player's and computer's final hands and scores
            print(
                f"\n\tYour cards:{player_cards}, current score: {sum_of_cards(player_cards)}"
            )
            print(
                f"\tComputer's cards: {computer_cards}, current score: {sum_of_cards(computer_cards)}"
            )

            # Determine the winner of the game based on the scores
            if (sum_of_cards(computer_cards) > 21):
                print("\nComputer went over. You win 😁\n")
            elif (sum_of_cards(computer_cards) > sum_of_cards(player_cards)):
                print("\nYou lose💀\n")
            elif (sum_of_cards(player_cards) > sum_of_cards(computer_cards)):
                print("\nYou win🙃\n")
            else:
                print("\nDraw🫠\n")
            condition = False

# Main game loop, asking if the player wants to play again
while input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
    play_game()  # Start a new game if the player enters 'y'
