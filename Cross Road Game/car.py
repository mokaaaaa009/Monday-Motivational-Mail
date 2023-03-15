from turtle import*
import random
DISTANCE=10
COLORS=['red','green','pink','yellow','purple','orange']

class Car:
    
    def __init__(self):
      self.SPEED=DISTANCE 
      self.Carlist = []
    def manufacture_car(self):
        car = Turtle()
        car.shape("square")
        car.penup()
        car.shapesize(1,2)
        y=random.randint(-250,250)
        color = random.choice(COLORS)
        car.color(color)
        car.goto(315,y)
        self.Carlist.append(car)
    
    def move(self):
      for car in self.Carlist:
        car.backward(self.SPEED)

    def levelUp(self):
      self.SPEED=self.SPEED+DISTANCE
  


    

  
      
      