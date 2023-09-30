# Import necessary classes from the coffee_maker, menu, and money_machine modules
from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

# Create instances of the Menu, CoffeeMaker, and MoneyMachine classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Initialize a flag to control the coffee machine's operation
coffee_machine_on = True

# Main loop to run the coffee machine until turned off
while coffee_machine_on:
    # Prompt the user for their drink choice and display the available menu items
    input1 = input(f"What would you like? ({menu.get_items()}): ")

    # Check if the user wants to turn off the coffee machine
    if input1 == "off":
        coffee_machine_on = False
    # Check if the user wants to generate a report
    elif input1 == "report":
        # Generate and display reports for the CoffeeMaker and MoneyMachine
        coffee_maker.report()
        money_machine.report()
    else:
        # Try to find the selected drink in the menu
        check = menu.find_drink(input1)
        if check is None:
            # If the drink is not in the menu, continue to the next iteration
            continue
        else:
            # Check if there are sufficient resources and if the user made a successful payment
            if coffee_maker.is_resource_sufficient(check) and money_machine.make_payment(check.cost):
                # If resources are sufficient and payment is successful, make the coffee
                coffee_maker.make_coffee(check)
