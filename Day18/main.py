from turtle import *
import heroes
import random

myScreen = Screen()
myTurtle = Turtle()

myTurtle.shape("turtle")
myTurtle.color("Green")
space=10
mycolors=["light sky blue","light blue","dark slate gray","light sky blue","medium aquamarine","dark green","peru","light sky blue","orange","firebrick","medium slate blue","magenta"]
moves=[1,2,3,4]

colormode(255)
myTurtle.speed(0)
myTurtle.hideturtle()
for i in range(int(360/10)):
  myTurtle.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
  myTurtle.right(10)
  myTurtle.circle(100)
myScreen.exitonclick()  
