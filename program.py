"""Coffee Machine App"""
from time import sleep
import sys
import beverages


def main():
    header()
    establish_resources()
    order = ask_for_order()
    set_drink(order)
    anything_else()
    turn_off()


def header():
    print()
    print()
    print('------------------------------------------------------------')
    print('              Welcome to the coffee shop')
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
    print('What do you want to drink: (1)Coffee, (2)Latte, (3)Cappucino')
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
    ask_for_order()


def set_drink(order):
    # Sets drinks class.
    if order == '1':
        drink = beverages.Coffee()
    elif order == '2':
        drink = beverages.Latte()
    else:
        drink = beverages.Cappuccino()
    print(f'You ordered a {drink.name}.\n')

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
    # Asks for payment.
    print(f'A {drink.name} costs ${drink.price}.')
    print('Please deposit coins')
    payment = 0
    while payment < drink.price:
        quarters = int(input('How many quarters will you deposit? '))
        payment = quarters * .25
        dimes = int(input('How many dimes will you deposit?'))
        payment = payment + dimes * .10
        nickels = int(input('How many dimes will you deposit?'))
        payment = payment + nickels * .05

    verify_transaction(payment)
    print('here is the money balance')
    anything_else()


def verify_transaction(payment):
    # Verifies if enough was paid and updates report.
    print('verified')
    make_drink(drink)


def make_drink(drink):
    # Updates report with resources used.
    print(resources)
    pass


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
