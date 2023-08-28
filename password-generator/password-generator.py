import random

# List of possible letters, numbers, and symbols
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Introduction
print("Welcome to the PyPassword Generator!")

# User input for the number of letters, symbols, and numbers in the password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Characters ordered as letters, symbols, and numbers:

# Initialize an empty string to store the generated password
string1 = ""

# Generate and add requested number of letters to the password
for letter in range(1, nr_letters + 1):
    string1 += random.choice(letters)

# Generate and add requested number of symbols to the password
for symbol in range(1, nr_symbols + 1):
    string1 += random.choice(symbols)

# Generate and add requested number of numbers to the password
for number in range(1, nr_numbers + 1):
    string1 += random.choice(numbers)

# Print the password with characters in the order they were generated
print(string1)
print("----------------")

# Hard Level - Characters ordered randomly:

# Initialize an empty list to store characters before shuffling
array = []
string2 = ""

# Generate and add requested number of letters to the list
for letter in range(1, nr_letters + 1):
    array.append(random.choice(letters))

# Generate and add requested number of symbols to the list
for symbol in range(1, nr_symbols + 1):
    array.append(random.choice(symbols))

# Generate and add requested number of numbers to the list
for number in range(1, nr_numbers + 1):
    array.append(random.choice(numbers))

# Shuffle the list to randomize the order of characters
random.shuffle(array)

# Convert the shuffled list to a string
for char in array:
    string2 += char

# Print the shuffled password
print(string2)
