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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

TOTAL_MONEY = 0
application = True


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${TOTAL_MONEY}")


def checking_resources(item):
    if item != "espresso":
        if MENU[item]['ingredients']['milk'] > resources['milk']:
            print("Sorry there is no enough milk")

    if MENU[item]['ingredients']["water"] > resources["water"]:
        print("Sorry there is not enough water")
    elif MENU[item]['ingredients']["coffee"] > resources["coffee"]:
        print("Sorry there is no enough coffee")
    else:
        checking_money(item)


def checking_money(item):
    global TOTAL_MONEY

    print("Please insert coins.")
    quarters_count = float(input("How many quarters?: ")) * 1/4
    dimes_count = float(input("How many dimes?: ")) * 1/10
    nickles_count = float(input("How many nickles?: ")) * 1/20
    pennies_count = float(input("How many pennies?: ")) * 1/100

    user_money = quarters_count + dimes_count + nickles_count + pennies_count
    if user_money < MENU[item]['cost']:
        print("Sorry that's not enough money. Money refunded")
    else:
        TOTAL_MONEY += MENU[item]['cost']
        user_money -= MENU[item]['cost']
        print(f"Enjoy your {item}☕")
        print(f"Here is ${user_money:.2f} dollars in change.")


def choice():
    global application

    which_one = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if which_one == "return":
        print_report()
    elif which_one == "off":
        application = False
    else:
        checking_resources(which_one)


while application:
    choice()
