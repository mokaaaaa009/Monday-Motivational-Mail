import turtle
ALIGNMENT="center"
FONT=("verdana", 40, "bold")

class Scoreboard (turtle.Turtle):
  
  def __init__(self):
    super().__init__()
    self.score1=0
    self.score2=0
    self.penup()
    self.hideturtle()
    self.goto(0, 130)
    self.write(f"{self.score1}     {self.score2}", align=ALIGNMENT, font=FONT)
      
  def update_score(self,xcor):
    self.clear()
    if xcor>340:
      self.score2+=1
    else:
      self.score1+=1
    self.write(f"{self.score1}     {self.score2}", align=ALIGNMENT, font=FONT)
    
  def game_over(self):
    self.clear()
    self.goto(0, 0)
    self.write(f"Game Over\n", align=ALIGNMENT, font=FONT)
    self.goto(0, -30)
    if self.score1>self.score2:
      self.write(f"Player 1 Win !!!!", align=ALIGNMENT, font=FONT)    
    else:
      self.write(f"Player 2 Win !!!!", align=ALIGNMENT, font=FONT)  

  




