# Import necessary modules
from replit import clear  # Import the 'clear' function from the 'replit' module
from art import logo  # Import the 'logo' variable from the 'art' module

# Initialize variables
other_bidders = True  # Flag to control the bidding loop
bidders = {}  # Dictionary to store bidders and their bids

# Function to find the bidder with the highest bid
def rich_bidder(biddings):
    rich_people = ""  # Initialize the winner's name
    max_money = 0  # Initialize the highest bid amount

    # Iterate through the dictionary of biddings
    for people in biddings:
        if (biddings[people] > max_money):  # Check if the current bid is higher
            rich_people = people  # Update the winner's name
            max_money = biddings[people]  # Update the highest bid amount
    
    # Print the winner's information
    print(f"The winner is {rich_people} with a bid of ${max_money}")

# Display the program's logo and welcome message
print(logo)
print("Welcome to the secret auction program")

# Bidding loop
while (other_bidders):
    name = input("What is your name?: ")  # Prompt for bidder's name
    bid = int(input("What is your bid?: $"))  # Prompt for bidder's bid
    bidders[name] = bid  # Store the bidder's information in the dictionary

    condition = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n")  # Check if there are more bidders
    if (condition == "no"):
        other_bidders = False  # Exit the bidding loop if there are no more bidders
    clear()  # Clear the screen for the next bidder

# Call the function to determine and display the winner
rich_bidder(bidders)
