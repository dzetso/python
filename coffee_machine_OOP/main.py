from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

a_menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

coffee_continue = True

while coffee_continue:
    answer = input(f"What would you like? ({a_menu.get_items()}): ")
    if answer == "report":
        coffee_maker.report()
        money_machine.report()
    elif answer == "off":
        coffee_continue = False
    else:
        order = a_menu.find_drink(answer)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
