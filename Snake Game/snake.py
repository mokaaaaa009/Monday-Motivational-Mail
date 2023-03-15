from turtle import *
import heroes
import random
import time


MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
POSISTIONS=[(0,0),(-20,0),(-40,0)]
class Snake:
  snake=[]
  def __init__(self) :
    self.snake=[]
    self.createSnake()
    self.head = self.snake[0]
    self.head.shape("square")
    self.head.color("green")
  
    
#create the snake according to the positions which is 3 blocks long
  def createSnake(self):
    for part in POSISTIONS:
     segment=Turtle("square")
     segment.color("black")
     segment.penup()
     segment.goto(part)
     self.snake.append(segment)
  
#Add to the Snake new blcok when eat the food
  def addSegment(self,position):
     segment=Turtle("square")
     segment.color("black")
     segment.penup()
     segment.goto(position)
     self.snake.append(segment)
  def detectCollision(self):
    if self.head.xcor()>290 or self.head.xcor()<-290 or self.head.ycor()>280 or self.head.ycor()<-290:
      return True
    for segment in self.snake[1:]:
      if self.head.distance(segment)<10:
        self.head.color("red")
        return True

  def reset(self):
    for segment in self.snake:
      segment.goto(1000,1000)
      segment.clear() 
    self.snake.clear()       
    self.createSnake()
    self.head = self.snake[0]  
    self.head.color("green")
     
            


   

  def extend (self):
    self.addSegment(self.snake[-1].position())
    
  def move(self):
    for segment in range(len(self.snake)-1,0,-1):
      newX=self.snake[segment-1].xcor()
      newY=self.snake[segment-1].ycor()
      self.snake[segment].goto(newX,newY)
    self.snake[0].forward(MOVE_DISTANCE)  

  def goUp(self):
    if self.snake[0].heading() != DOWN:
      self.snake[0].setheading(UP)
      
  def moveleft(self):
    if self.snake[0].heading() != RIGHT: 
      self.snake[0].setheading(LEFT)
      
  def moveright(self):
    if self.snake[0].heading() != LEFT: 
      self.snake[0].setheading(RIGHT)
      
  
  def movedown(self):
    if self.snake[0].heading() != UP: 
      self.snake[0].setheading(DOWN)
      

