# refactor coffee machine into OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()



print("Welcome to the Python Coffee Machine!")

bev = menu.find_drink(input(f"What would you like to order? {menu.get_items()}? "))

operating = True

while operating:
    if bev == "report":
        coffee_maker.report()
        money_machine.report()
    elif bev == "off":
        operating = False
    elif coffee_maker.is_resource_sufficient(menu.find_drink(bev)):
        money_machine.process_coins()
        coffee_maker.make_coffee(bev.name)
    else:
        operating = False
