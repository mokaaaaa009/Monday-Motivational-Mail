from turtle import *

class game_Screen:
  def __init__(self):
    self.screen = Screen()
    self.Dashline = Turtle()
  def start(self):
    self.screen.bgcolor("blue")
    self.screen.setup(width = 800, height = 400)
    self.screen.tracer(0)
    self.screen.title("Pong Game")
    self.Dashline.hideturtle()
    self.Dashline.up()
    self.Dashline.width(6)
    self.Dashline.setpos(0,210)
    self.Dashline.setheading(270)
    self.Dashline.up()
    for _ in range(20):
      self.Dashline.forward(10)
      self.Dashline.up()
      self.Dashline.forward(10)
      self.Dashline.down()   
    self.screen.update()
    self.screen.exitonclick()
      

