from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

keep_going = True

while keep_going:
    drink_name = input(f"What would you like? ({menu.get_items()}): ").lower()
    if drink_name == "off":
        print("Turning off. Bye!")
        keep_going = False
    elif drink_name == "report":
        coffee_maker.report()
        money_machine.report()
    elif drink_name in menu.get_items().split('/'):
        drink = menu.find_drink(drink_name)
        if coffee_maker.is_resource_sufficient(drink):
            print(f"A {drink_name} costs ${drink.cost:.2f}.")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print(f"I didn't understand your choice, '{drink_name}', please try again.")
