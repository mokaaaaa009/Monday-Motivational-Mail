import coffe
import os


#Requesting and taking coins from customer and return change
def takingCoins(order,MENU):
  '''Display to User to enter his coins and return the total amount of what user paid '''
  print("Please enter coins !!!")
  quarters=float(input("How many quarters? "))
  dimes=float (input("How many dimes? "))
  nickel=float(input("How many nickel? "))
  pennies=float(input("How many pennies? "))
  total=quarters*0.25+dimes*0.10+nickel*0.05+pennies*0.01
  return total


#check if coffe machine have enough resources 
def checkOrder(order,RESOURCES,MENU):
  '''Check what kind of order has been orderd and then compare it to the current resources 
     and return true if it's enough flase if it's not and print message'''
  ingredients = MENU[order]['ingredients']
  for ingredient in ingredients:
    if ingredients[ingredient]>RESOURCES[ingredient]:
      print(f"Sorry there is not enough {ingredient}")
      return False
  return True

#after payment we deducte from the resources and make coffee
def makeCoffee(order,MENU,RESOURCES):
  orderingredients = MENU[order]['ingredients']
  for ingredient in orderingredients:
    RESOURCES[ingredient]=RESOURCES[ingredient]-orderingredients[ingredient]
  return RESOURCES  

collection=0
MENU=coffe.MENU
RESOURCES=coffe.resources
ESPRESSO=MENU['espresso']['cost']
LATTE=MENU['latte']['cost']
CAPPUCCINO=MENU['cappuccino']['cost']
flage=True
off=True
# TODO:1 Ask User what he want
while(off):
 order=input(f"What would you like ? (espresso {ESPRESSO}$/latte {LATTE}$/cappuccino {CAPPUCCINO}$): ")
#  TODO:4 Print Report  
 if order.lower() == "report":
   print(f"Water : {RESOURCES['water']}ml")
   print(f"Milk : {RESOURCES['milk']}ml")
   print(f"Coffe : {RESOURCES['coffee']}mg")
   print(f"Money : {collection}$")  
 elif order.lower() == "off":
  off=False
 else:
# TODO:5 Check Resource suffecient 
  valid=checkOrder(order,RESOURCES,MENU)
  if valid:
    coins=takingCoins(order,MENU)
    if coins<MENU[order]['cost']:
      print("Sorry that's not enough money . Money Refunded.")
      flage=False
    else:
      collection+=MENU[order]['cost']
      change=coins-MENU[order]['cost']      

#TODO:8 Make Coffee
    if flage:
      RESOURCES=makeCoffee(order,MENU,RESOURCES)
      if float(coins) > 0.00:
       print(f"Here's your {change} dollars change.")
       print(f"Here's your {order}. Enjoy!!!")
    flage=True   
# TODO:3 Turn Off the Coffee Machine 





