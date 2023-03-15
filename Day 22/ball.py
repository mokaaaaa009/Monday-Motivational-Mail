from turtle import *

class Ball(Turtle):
    def __init__(self):
      super().__init__()
    def createBall(self):
      self.shape("circle")
      self.color("white")
      self.penup()
      self.moveX=10
      self.moveY=10
      self.moveSpeed=0.1
      
      
    def moveBall(self):
        x=self.xcor()+self.moveX
        y=self.ycor()+self.moveY
        self.goto(x,y)

    def bounce(self):
      if self.ycor() == 180 or self.ycor() == -180:
        self.moveY=self.moveY*-1
    def xbounce(self):
        self.moveX*=-1
        self.moveSpeed *=0.9       
    
    
    
    def checkloss(self):
      if self.xcor() > 350 or self.xcor() < -350:   
        return True
      return False

            
          
          





        
     
    

      
      