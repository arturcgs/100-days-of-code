from data import MENU, resources
from art import logo


def check_resources(beverage):
    """Return list of missing ingredients
    Return empty list if no missing ingredient"""
    missing = []
    for ingredient, menu_quantity in MENU[beverage]['ingredients'].items():
        if menu_quantity > resources[ingredient]:
            missing.append(ingredient)
    return missing


def ask_for_money():
    """Asks the user for money, and sums the ammount"""
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.1
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickles + pennies


def change_resources(beverage, machine_assets):
    """Subtracts the beverage ingredients from the machine's resources"""
    # add money
    machine_assets['money'] += MENU[beverage]['cost']
    # remove ingredients
    for ingredient, menu_quantity in MENU[beverage]['ingredients'].items():
        machine_assets[ingredient] -= menu_quantity
    return machine_assets


# print logo
print(logo)

# initiating on
on = True

while on:
    # print menu
    print("\nEspresso: $1.5\nLatte: $2.5\nCappuccino: $3.0\n")
    # ask for the drink
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

    # report
    if drink == 'report':
        for key, item in resources.items():
            if key in ['water', 'milk']:
                print(f"{key.capitalize()}: {item}mL")
            elif key == 'coffee':
                print(f"{key.capitalize()}: {item}g")
            elif key == 'money':
                print(f"{key.capitalize()}: ${item:.2f}")

    # turn off
    elif drink == 'off':
        print('turning off...')
        on = False

    # actual drink
    elif drink in MENU.keys():
        # check if the machine has all ingredients
        missing_ingredients = check_resources(drink)
        if missing_ingredients:
            print(f"Sorry, we are missing {', '.join(missing_ingredients).title()}")
        # if it can make the drink
        else:
            # saving drink cost and printing it
            drink_cost = MENU[drink]['cost']
            print(f"Your drink costs ${drink_cost:.2f}")
            # asking for money
            money_received = ask_for_money()
            # check if the gave enough money
            if money_received >= drink_cost:
                # show how much they gave
                print(f"You gave ${money_received:.2f}")
                if money_received != drink_cost:
                    # give change
                    print(f"Here is your change: ${(money_received - drink_cost):.2f}")
                # give drink
                print(f"Here is your {drink}, hope you enjoy it! ☕")
                # change resources
                change_resources(drink, resources)
            else:
                print(f"Sorry, you don't have enough money. Here is your refund: ${money_received:.2f}")

    # invalid command
    else:
        print("Invalid command")
