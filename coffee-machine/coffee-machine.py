# Define the menu items and their ingredients and costs
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Define the initial resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Initialize the total money earned
TOTAL_MONEY = 0

# Initialize the application state
application = True

# Function to print the current resource status and total money
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${TOTAL_MONEY}")

# Function to check if there are enough resources for the selected item
def checking_resources(item):
    global resources

    # Check milk availability for items other than espresso
    if item != "espresso":
        if MENU[item]['ingredients']['milk'] > resources['milk']:
            print("Sorry there is not enough milk")

    # Check water and coffee availability
    if MENU[item]['ingredients']["water"] > resources["water"]:
        print("Sorry there is not enough water")
    elif MENU[item]['ingredients']["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee")
    else:
        # Deduct used resources
        if item != "espresso":
            resources["milk"] -= MENU[item]['ingredients']['milk']
        resources["water"] -= MENU[item]['ingredients']['water']
        resources["coffee"] -= MENU[item]['ingredients']['coffee']

        # Check money and proceed to make the drink
        checking_money(item)

# Function to check if the user has inserted enough money
def checking_money(item):
    global TOTAL_MONEY

    print("Please insert coins.")
    quarters_count = float(input("How many quarters?: ")) * 1/4
    dimes_count = float(input("How many dimes?: ")) * 1/10
    nickels_count = float(input("How many nickels?: ")) * 1/20
    pennies_count = float(input("How many pennies?: ")) * 1/100

    user_money = quarters_count + dimes_count + nickels_count + pennies_count
    if user_money < MENU[item]['cost']:
        print("Sorry that's not enough money. Money refunded")
    else:
        # Update total money and provide change
        TOTAL_MONEY += MENU[item]['cost']
        user_money -= MENU[item]['cost']

        print(f"Enjoy your {item}☕")
        print(f"Here is ${user_money:.2f} dollars in change.")

# Function to handle user's choice
def choice():
    global application

    which_one = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if which_one == "report":
        print_report()
    elif which_one == "off":
        application = False
    else:
        checking_resources(which_one)

# Main program loop
while application:
    choice()
