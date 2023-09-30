from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_machine_on = True

while coffee_machine_on:
    input1 = input(f"What would you like? ({menu.get_items()}): ")

    if input1 == "off":
        coffee_machine_on = False
    elif input1 == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        check = menu.find_drink(input1)
        if check is None:
            continue
        else:
            if coffee_maker.is_resource_sufficient(check) and money_machine.make_payment(check.cost):
                coffee_maker.make_coffee(check)
