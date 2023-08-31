# Import the 'logo' from the 'ceaser_art' module for display
from ceaser_art import logo
# Import 'clear' function from the 'replit' module for clearing the console
from replit import clear

# Define the alphabet for reference
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Display the logo
print(logo)

# Set the initial state of the game
game_on = True

# Start the main loop
while game_on:
    # Get the user's choice for encoding or decoding
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Get the text to be processed from the user
    text = input("Type your message:\n").lower()
    # Get the shift value for the Caesar cipher
    shift = int(input("Type the shift number:\n"))
    
    # Define a function to perform the Caesar cipher
    def caesar(text, shift, direction):
        string = ""
        if direction == "decode":
            shift *= -1  # Adjust shift for decoding
        for char in text:
            if char in alphabet:
                # Apply the Caesar cipher shift and handle wrapping around the alphabet
                string += alphabet[(alphabet.index(char) + shift) % len(alphabet)]
            else:
                string += char  # Keep non-alphabet characters unchanged
        
        # Display the result
        print(f"The {direction}d text is: {string}")

    # Call the caesar function to process the text
    caesar(text, shift, direction)
    
    # Ask the user if they want to restart the cipher program
    condition = input("Do you want to restart the cipher program?: ").lower()
    
    # Clear the console for a clean interface
    clear()
    
    # Check the user's response to determine whether to continue or exit the loop
    if condition == "no":
        print("Goodbye")
        game_on = False  # Exit the loop and end the program
