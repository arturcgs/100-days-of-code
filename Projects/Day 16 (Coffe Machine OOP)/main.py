from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_controller = MoneyMachine()

is_on = True

while is_on:
    print(f"Choose one of these drinks: {menu.get_items()}")
    drink_choice = input("What drink would you like? ").lower().strip()

    if drink_choice == 'off':
        print("Turning off.....")
        is_on = False

    elif drink_choice == 'report':
        coffee_machine.report()
        money_controller.report()

    else:
        drink_obj = menu.find_drink(drink_choice)
        if drink_obj and coffee_machine.is_resource_sufficient(drink_obj) \
                and money_controller.make_payment(drink_obj.cost):
            coffee_machine.make_coffee(drink_obj)









