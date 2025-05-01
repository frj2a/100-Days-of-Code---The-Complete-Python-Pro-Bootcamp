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

coins = {
    "penny": 0.01,
    "nickle": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}

profit = 0
keep_going = True


def has_resources(recipe):
    """Returns if resource needed by ingredients dictionary is available in stock"""
    global resources
    result = True
    for resource in recipe:
        if recipe[resource] > resources[resource]:
            print(f"Sorry, there is not enough {resource} in the machine")
            result = False
    return result

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = 0
    for coin in coins:
       total += int(input(f"how many {coin}s?: ")) * coins[coin]
    return total

def update_resources(recipe):
    global resources
    for resource in recipe:
        resources[resource] -= recipe[resource]

def print_report():
    global resources
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    print(f"Money: ${profit:.2f}")

while keep_going:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink == "off":
        print("Turning off. Bye!")
        keep_going = False
    elif drink == "report":
        print_report()
    elif drink in MENU.keys():
        ingredients = MENU[drink]["ingredients"]

        if has_resources(ingredients):
            cost = MENU[drink]["cost"]
            print(f"A {drink} costs ${cost:.2f}, please insert coins for payment:")
            payment = process_coins()
            if payment >= cost:
                if payment == cost:
                    print("Exact payment, thank you!")
                else:
                    print(f"Thank you! Your change is ${(payment - cost):.2f}")
                profit += cost
                update_resources(ingredients)
                print(f"Here is your {drink}. Enjoy!")
            else:
                print (f"Payment of ${payment} is not enough. Money refunded.")
    else:
        print(f"I didn't understand your choice, '{drink}', please try again.")
