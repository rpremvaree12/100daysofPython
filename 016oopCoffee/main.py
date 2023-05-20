# refactor coffee machine into OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

print("Welcome to the Python Coffee Machine!")


is_operating = True

while is_operating:
    order = input(f"What would you like to order? {menu.get_items()}? ")
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        is_operating = False
    else:
        bev = menu.find_drink(bev)
        if coffee_maker.is_resource_sufficient(drink=):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)
