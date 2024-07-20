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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 4. Check resources sufficient?
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True


# TODO: 5. Process coins.
def process_coins() -> object:
    """Returns the total calculated from coins inserted."""
    print('Please insert coins:')
    total = int(input('Number of Quarters: ')) * 0.25
    total += int(input('Number of Dimes: ')) * 0.1
    total += int(input('Number of Nickels: ')) * 0.05
    total += int(input('Number of Pennies: ')) * 0.01
    return total


# TODO: 6. Check transaction successful?
def is_transaction_successful(money_received , coffee_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= coffee_cost:
        change = round(money_received - coffee_cost, 2)
        print(f'Here is ${change} in change.')
        global profit
        profit += coffee_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: 7. Make Coffee.
def make_coffee(coffee_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee_name}! ☕\n")


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.


is_on = True

while is_on:
    print('Welcome to the Coffee Machine!\nPrices:\n Espresso:$1.50\n Latte: $2.50\n Cappuccino: $3\n')
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        is_on = False
    # TODO: 3. Print report
    elif choice == 'report':
        print(f'Water: {resources["water"]}')
        print(f'Milk: {resources["milk"]}')
        print(f'Coffee: {resources["coffee"]}')
        print(f'Money: ${profit}')
    else:
        coffee = MENU[choice]
        if is_resource_sufficient(coffee['ingredients']):
            payment: object = process_coins()
            if is_transaction_successful(payment, coffee["cost"]):
                make_coffee(choice, coffee['ingredients'])



