from menu import Menu 
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items = Menu()
barista=CoffeeMaker()
accountant=MoneyMachine()
on = True
ESPRESSO = items.find_drink("espresso")
LATTE =items.find_drink("latte")
CAPPUCCINO=items.find_drink("cappuccino")
while(on):
  order=input(f"What would you like ? (espresso {ESPRESSO.cost}$/latte {LATTE.cost}$/cappuccino {CAPPUCCINO.cost}$): ")
  if order == "off":
    on=False
  elif order == "report":
    barista.report()
    accountant.report()
  else:
    newcoffee=items.find_drink(order)
    if  newcoffee != None:
      if barista.is_resource_sufficient(newcoffee):
        if accountant.make_payment(newcoffee.cost):
          barista.make_coffee(newcoffee)



















