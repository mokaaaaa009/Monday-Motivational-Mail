from turtle import *

class Paddle(Turtle):
    
    def __init__(self,x,y):
      super().__init__()
      self.setup(x,y)
    def setup(self,x,y):
      self.shape("square")
      self.color("white")
      self.shapesize(4,1)
      self.penup()
      self.goto(x,y)
      self.speed("fastest")

    def goUp(self):
      self.goto(self.xcor(),self.ycor()+20)
    def goDown(self):
      self.goto(self.xcor(),self.ycor()-20) 

   
