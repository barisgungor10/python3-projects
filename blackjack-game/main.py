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

##################### Hints #####################
import random
from replit import clear
from art import logo

def play_game():
        clear()
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
        def random_card():
            return random.choice(cards)
    
        def sum_of_cards(cards):
            sum = 0
            for card in cards:
                sum += card
            return sum

        def convert_ace(cards):
            for number in range(len(cards)-1):
                if(cards[number] == 11):
                    cards[number] = 1
                
        player_cards = [ random_card(), random_card() ]
        computer_cards = [random_card(), random_card() ]
    
        print(logo)
        print(f"\n\tYour cards:{player_cards}, current score: {sum_of_cards(player_cards)}")
        print(f"\tComputer's first card: {computer_cards[0]}")

        condition = True
        while condition:
            take_card = input("\nType 'y' to get another card, type 'n' to pass: ")
            if take_card == 'y':
                player_cards.append(random_card())
                if 11 in player_cards and sum_of_cards(player_cards) > 21:
                    convert_ace(player_cards)
                    
                print(f"\tYour cards:{player_cards}, current score: {sum_of_cards(player_cards)}")
                print(f"\tComputer's first card: {computer_cards[0]}")
                
                if sum_of_cards(player_cards) > 21:
                    print("\nYou went over. You lose😭")
                    condition = False
            elif take_card == 'n':
    
                while sum_of_cards(computer_cards) < 17:
                    if 11 in computer_cards and sum_of_cards(computer_cards) > 21:
                        convert_ace(computer_cards)
                    computer_cards.append(random_card())
                    
                print(f"\tYour cards:{player_cards}, current score: {sum_of_cards(player_cards)}")
                print(f"\tComputer's cards: {computer_cards}, current score: {sum_of_cards(computer_cards)}")
                
                if(sum_of_cards(computer_cards) > 21):
                    print("\nComputer went over. You win 😁")
                elif(sum_of_cards(computer_cards) > sum_of_cards(player_cards)):
                    print("\nYou lose")
                elif(sum_of_cards(player_cards) > sum_of_cards(computer_cards)):
                    print("\nYou win")
                else:
                    print("\nDraw")
                condition = False

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
    play_game()