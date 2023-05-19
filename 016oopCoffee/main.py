# refactor coffee machine into OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


print(menu.get_items())

bev = input("Would you like an espresso, latte or cappuccino? ").lower()
# menu.find_drink(bev)

if bev == "report":
    menu.report()
    money_machine.report()