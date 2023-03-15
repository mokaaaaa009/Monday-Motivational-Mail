from turtle import Turtle
import random

class Food (Turtle):
 def __init__(self):
   super().__init__()
   self.shape("circle")
   self.penup()
   self.shapesize(stretch_len=0.5,stretch_wid=0.5)
   self.color("blue")
   self.speed("fastest")
   randPosX=random.randint(-280,280)
   randPosY=random.randint(-280,280)
   self.goto(randPosX,randPosY)
 def gameOver(self):
  self.hideturtle()
 def setNewPos(self):
  randPosX=random.randint(-280,280)
  randPosY=random.randint(-280,280)
  self.goto(randPosX,randPosY)



    





