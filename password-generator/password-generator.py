#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomised:
string1 = ""
for letter in range(1, nr_letters + 1):
    string1 += random.choice(letters)
for symbol in range(1, nr_symbols + 1):
    string1 += random.choice(symbols)
for number in range(1, nr_numbers + 1):
    string1 += random.choice(numbers)
print(string1)
print("----------------")
#Hard Level - Order of characters randomised:
array = []
string2 = ""
for letter in range(1, nr_letters + 1):
    array.append(random.choice(letters))
for symbol in range(1, nr_symbols + 1):
    array.append(random.choice(symbols))
for number in range(1, nr_numbers + 1):
    array.append(random.choice(numbers))
random.shuffle(array)

for char in array:
    string2 += char
print(string2)