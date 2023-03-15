from turtle import *
import heroes
import random
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard
import keyboard

snakeList=[]
myScreen = Screen()
snake=Snake()
myScreen.setup(width=600,height=600)
myScreen.tracer(0)
score=Scoreboard()
startgame=True
sFood=Food()


while(startgame):
  
  snake.move()
  time.sleep(0.1)
  myScreen.update()
  if snake.head.distance(sFood)<15:
    sFood.setNewPos()
    snake.extend()
    score.update_score()
  myScreen.listen()
  myScreen.onkeypress(snake.goUp,"Up")  
  myScreen.onkeypress(snake.moveleft,"Left")  
  myScreen.onkeypress(snake.moveright,"Right")  
  myScreen.onkeypress(snake.movedown,"Down")  
  if snake.detectCollision():
    score.reset()
    snake.reset()
    for i in range(5,0,-1):
      Timer = Turtle()
      Timer.hideturtle()
      Timer.up()
      Timer.goto(-120,10)
      Timer.write(f"Press e key to exit\n",font=("Arial",20,"normal"))
      Timer.goto(0,10)
      Timer.write(str(i),font=("Arial",20,"normal"))
      time.sleep(1)
      myScreen.update()
      Timer.clear()
      if keyboard.is_pressed("e"):
        startgame=False
        break
  
myScreen.update()  
myScreen.exitonclick()
