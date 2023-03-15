from turtle import*

DISTANCE=10
class Hero(Turtle):
    def __init__(self):
      super().__init__()
      self.shape("turtle")
      self.penup()
      self.color("green")
      self.goto(0,-280)
      self.setheading(90)
      self.moveY=10
    def goUp(self):
      self.forward(DISTANCE)
    def goDown(self):
      self.backward(DISTANCE)
    def goRight(self):
      self.goto(self.xcor()+DISTANCE,self.ycor())  
    def goLeft(self):
      self.goto(self.xcor()-DISTANCE,self.ycor())    

      



