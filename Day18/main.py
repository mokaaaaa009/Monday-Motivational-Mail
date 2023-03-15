from turtle import *
import heroes
import random

myScreen = Screen()
myTurtle = Turtle()

myTurtle.shape("turtle")
myTurtle.color("Green")
space=10
# myTurtle.penup()
# myTurtle.setposition(-250,0)
# myTurtle.pendown()
# myTurtle.showturtle()
# for i in range(5):
#  for _ in range(10):
#   myTurtle.forward(space)
#   myTurtle.penup()
#   myTurtle.forward(space)
#   myTurtle.pendown()
 
#  myTurtle.penup() 
#  i*=10
#  myTurtle.setposition(-250,-i)


# def shapeDraw(sides,mycolors):
#   angle=360/sides
#   myTurtle.color(mycolors[sides])
#   for _ in range(sides):

#     myTurtle.forward(100)
#     myTurtle.right(angle)
  
mycolors=["light sky blue","light blue","dark slate gray","light sky blue","medium aquamarine","dark green","peru","light sky blue","orange","firebrick","medium slate blue","magenta"]
# for sides in range(3,11):
#   shapeDraw(sides,mycolors)
moves=[1,2,3,4]

colormode(255)
#for _ in range(200):
  
  # move=random.choice(moves)
  # if move==1:
  #   myTurtle.right(90)
  #   myTurtle.forward(20)
  # elif move==2:  
  #   myTurtle.right(90)
  #   myTurtle.backward(20)
  # elif move == 3:
  #   myTurtle.left(90)
  #   myTurtle.forward(20)
  # else:
  #   myTurtle.left(90)
  #   myTurtle.backward(20)

# direction=[0,90,180,270]
# for _ in range(10):
#   myTurtle.setheading(random.choice(direction))
#   myTurtle.forward(20)
myTurtle.speed(0)
myTurtle.hideturtle()
for i in range(int(360/10)):
  myTurtle.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
  myTurtle.right(10)
  myTurtle.circle(100)
myScreen.exitonclick()  
