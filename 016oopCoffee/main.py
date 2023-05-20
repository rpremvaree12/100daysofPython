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
    bev = input(f"What would you like to order? {menu.get_items()}? ")
    if bev == "report":
        coffee_maker.report()
        money_machine.report()
    elif bev == "off":
        is_operating = False
    else:
        menu.find_drink(bev)
        if coffee_maker.is_resource_sufficient(menu.find_drink(bev)):
            money_machine.make_payment(menu.find_drink(bev).cost)
            coffee_maker.make_coffee(menu.find_drink(bev))
