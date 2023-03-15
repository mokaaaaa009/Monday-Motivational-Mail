from turtle import *
import heroes
import random

myScreen = Screen()
myTurtle = Turtle()

def moveright():
  myTurtle.forward(10)
def moveleft():
  myTurtle.backward(10)
def moveclockwise():
  myTurtle.right(10) 
def movecounterclockwise():
  myTurtle.left(10)  
def clear():
  myTurtle.setposition(0,0)
  myTurtle.penup()
  myTurtle.clear()
  myTurtle.setheading(0)
       
myScreen.listen()
myScreen.onkeypress(moveright,"w")
myScreen.onkeypress(moveleft,"s")
myScreen.onkeypress(moveclockwise,"d")
myScreen.onkeypress(movecounterclockwise,"a")
myScreen.onkey(clear,"c")


myScreen.exitonclick()
