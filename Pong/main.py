from turtle import *
import time
from Game_Screen import game_Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


def startGame(screen):
    Dashline=Turtle()
    Dashline.hideturtle()
    screen.bgcolor("blue")
    screen.setup(width = 800, height = 400)
    screen.title("Pong Game")
    screen.tracer(0)
    Dashline.up()
    Dashline.width(6)
    Dashline.setpos(0,210)
    Dashline.setheading(270)
    Dashline.up()
    for _ in range(20):
      Dashline.forward(10)
      Dashline.up()
      Dashline.forward(10)
      Dashline.down()
score=Scoreboard()
ball=Ball()
ball.createBall()        
screen= Screen()
startGame(screen)
player1=Paddle(350,0)
player2=Paddle(-350,0)
screen.listen()
screen.onkeypress(player2.goUp,"w")
screen.onkeypress(player2.goDown,"s")
screen.onkeypress(player1.goUp,"Up")
screen.onkeypress(player1.goDown,"Down")
gameIson=0
while gameIson<5:
  time.sleep(ball.moveSpeed)
  ball.moveBall()
  ball.bounce()
  if ball.distance(player1) <50 and ball.xcor() > 320 or ball.distance(player2) <50 and ball.xcor() < -320:
    ball.xbounce()
  if ball.checkloss():
    score.update_score(ball.xcor())
    ball.goto(0,0)
    player1.goto(350,0)
    player2.goto(-350,0)
    gameIson+=1
    if gameIson==5:
      score.game_over()
  
  screen.update()
screen.exitonclick()
  














