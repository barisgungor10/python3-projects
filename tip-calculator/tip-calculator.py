#welcome message
print("Welcome to the tip calculator.")
#asking user the bill
bill = float( input("What was the total bill? $") )
#asking what percentage tip would you like to give? to user
percentage = int( input("What percentage tip would you like to give? ") ) / 100
#asking How many person to split the bill? to user
person = int( input("How many person to split the bill? ") )
#printing the value of each person should pay
print(f"Each person should pay {round((bill + (bill*percentage)) / person, 2):.2f}")