from turtle import *
from hero import Hero
import time
import random
from  car import Car
from scoreBoard import Scoreboard
LEVEL =0.1
screen= Screen()
screen.bgcolor("white")
screen.setup(width = 600, height = 600)
screen.title("Turtle Crossing")
score=Scoreboard()
screen.tracer(0)
obstacl=Car()
myHero=Hero()
screen.listen()
screen.onkeypress(myHero.goUp, "Up")
screen.onkeypress(myHero.goDown, "Down")
screen.onkeypress(myHero.goRight, "Right")
screen.onkeypress(myHero.goLeft, "Left")
gameisOn=True
factory=Car()
while gameisOn:
  time.sleep(LEVEL)  
  screen.update()
  factory.manufacture_car()
  factory.move()
  for car in factory.Carlist:
    if car.xcor()>390 or car.xcor()<-390:
      car.clear()
    if car.distance(myHero) < 20:
      screen.clear()
      score.game_over()
      gameisOn=False
      screen.update()
  if myHero.ycor() >270:
     myHero.goto(0,-280)
     factory.levelUp()
     score.update_score()
  elif myHero.ycor() <-270:
     myHero.goto(myHero.xcor(),-270)
           
     


  
screen.exitonclick()
