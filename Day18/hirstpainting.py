import random
from turtle import *
import colorgram
import os


myScreen = Screen()
myTurtle = Turtle()

myTurtle.shape('arrow')
# colors = colorgram.extract('spots.jpg', 30)
# myColors=[]
# for color in colors:
#   firstColor=color.rgb
#   r=firstColor.r
#   g=firstColor.g
#   b=firstColor.b
#   myColors.append((r,g,b))
# print(myColors)

colormode(255)
mycolors=[(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]
myTurtle.up()
myTurtle.setpos(0,-255)
myTurtle.speed(0)
for i in range(10):
   for j in range(10):
     myColor=random.choice(mycolors)
     myTurtle.pencolor(myColor)
     myTurtle.dot(10)
     myTurtle.forward(30)
   myTurtle.setheading(90)
   myTurtle.forward(50)
   myposx=myTurtle.xcor()
   myposy=myTurtle.ycor()
   myTurtle.setpos(myposx-300,myposy)
   myTurtle.setheading(0)

  
   
myScreen.exitonclick() 
