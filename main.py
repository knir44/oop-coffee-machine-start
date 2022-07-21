from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    off = False
    coffee_makers = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()

    while not off:
        wish = input(f"What would you like to drink? Type {menu.get_items()}: ").lower()
        if wish == "off":
            off = True
            print("Turning off...")

        elif wish == "report":
            coffee_makers.report()
        else:
            wish = menu.find_drink(wish)
            if wish != "none":
                if coffee_makers.is_resource_sufficient(wish):
                    if  money_machine.make_payment(wish.cost):
                        coffee_makers.make_coffee(wish)


coffee_machine()

