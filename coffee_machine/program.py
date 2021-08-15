"""Coffee Machine App"""
from time import sleep
import sys
import beverages
from random import randint


def main():
    header()
    establish_resources()
    order = ask_for_order()
    set_drink(order)
    anything_else()
    turn_off()


def header():
    print()
    print('------------------------------------------------------------')
    print()
    print('              Welcome to the coffee shop')
    print()
    print('------------------------------------------------------------')
    print()
    print()


def establish_resources():
    # Establishes startging resources in ml and dollars.
    global resources
    resources = {'Water': 800,
                 'Milk': 800,
                 'Coffee': 500,
                 'Money': 30}


def ask_for_order():
    # Asks user for order.
    tab = '    '
    print(
        f'What do you want to drink: \n {tab}  (1)Coffee\n {tab}  (2)Latte\n {tab}  (3)Cappucino')
    order = input().strip()
    if order == 'report':
        view_report()
    if order == 'off':
        turn_off()
    while order not in ('1', '2', '3'):
        order = input('\nPlease enter 1, 2 or 3. \n ')

    return order


def view_report():
    print(resources)
    print()
    sleep(3)
    ask_for_order()


def set_drink(order):
    # Sets drinks class.
    if order == '1':
        drink = beverages.Coffee()
    elif order == '2':
        drink = beverages.Latte()
    else:
        drink = beverages.Cappuccino()
    print(f'\nYou ordered a {drink.name}.\n')

    response = verify_resources(drink)

    if response == True:
        process_money(drink)
    else:
        print(f"Sorry we don't have enough resources to make your {drink}.")
        anything_else()


def verify_resources(drink):
    # Verifies if resources are available to make drink.
    if drink.water > resources['Water']:
        return False
    elif drink.milk > resources['Milk']:
        return False
    elif drink.coffee > resources['Coffee']:
        return False
    else:
        return True


def process_money(drink):
    # Asks for payment. Determines if enough has been paid.
    print(f'A {drink.name} costs ${drink.price}.')
    print('Please deposit coins\n')
    payment = float()

    while payment < drink.price:
        payment = add_coins(payment)
        if payment < drink.price:
            print(f"\nThat only makes ${format(payment, '.2f')} ")
            message = ("You need to add mo money!", "You're too short man!",
                       "Come on pull out that paper stack.", "Keep it coming shawtee!")
            print(message[randint(0, 3)])
            print()

    print(f"\nThat makes ${format(payment, '.2f')}")
    change = format((payment - drink.price), '.2f')
    print(f'Here is your change: ${change}')
    print(f"\nLet's make that {drink.name}.\n")
    verify_transaction(drink)

    anything_else()


def add_coins(payment):
    sleep(1)
    tab = '    '
    quarters = int(input(tab + 'How many quarters will you deposit? '))
    payment = quarters * .25
    dimes = int(input(tab + 'How many dimes will you deposit? '))
    payment = payment + dimes * .10
    nickels = int(input(tab + 'How many nickels will you deposit?  '))
    payment = payment + nickels * .05
    return payment


def verify_transaction(drink):
    resources['Money'] = resources['Money'] + drink.price
    resources['Milk'] = resources['Milk'] - drink.milk
    resources['Water'] = resources['Water'] - drink.water
    resources['Coffee'] = resources['Coffee'] - drink.coffee
    make_drink(drink)


def make_drink(drink):
    # Updates report with resources used.
    print(f'Enjoy your {drink.name} ')
    print('Would you like anything else? y/n ')
    answer = input().lower().strip()
    if answer == 'report':
        for key, item in resources.items():
            print(key, item)
    elif answer == 'y':
        anything_else()
    else:
        turn_off()


def anything_else():
    # Prompts user if they want another drink.
    print('Do you want another drink? y/n ')
    answer = input().strip().lower()
    if answer == 'y':
        ask_for_order()
    else:
        turn_off()


def turn_off():
    print()
    sleep(.4)
    sys.exit("-----  Shutting down machine.  -----")


if __name__ == "__main__":
    main()
