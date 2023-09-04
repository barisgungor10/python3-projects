# Import necessary modules
from replit import clear  # Clears the console screen
from art import logo  # Imports the logo from the 'art' module

# Define functions for basic arithmetic operations
def add(number_1, number_2):
    return number_1 + number_2

def substract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

# Create a dictionary that maps operators to their respective functions
function_dictionary = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide 
}

# Define the main calculator function
def calculator():
    loop = True  # Initialize a loop control variable
    print(logo)  # Print the calculator logo
    
    # Get the first number from the user
    number_1 = float(input("What is the first number: "))
    
    # Main calculation loop
    while loop:
        # Get the arithmetic operation from the user
        operation = input("+\n-\n*\n/\nPick an operation: ")
        
        # Get the second number from the user
        number_2 = float(input("What is the next number: "))
        
        # Perform the calculation based on the selected operation
        result = function_dictionary[operation](number_1, number_2)
    
        # Display the result
        print(f"{number_1} {operation} {number_2} = {result}")
        
        # Ask the user if they want to continue or start a new calculation
        decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        
        if decision == 'y':
            number_1 = result  # Update the first number with the result
        elif decision == 'n':
            clear()  # Clear the console screen
            calculator()  # Start a new calculation by calling the calculator function recursively
            loop = False  # Exit the loop
            
# Call the calculator function to start the program
calculator()
