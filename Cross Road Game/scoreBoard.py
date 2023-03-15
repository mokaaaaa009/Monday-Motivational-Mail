import turtle
ALIGNMENT="center"
FONT=("verdana", 20, "bold")

class Scoreboard (turtle.Turtle):
  
  def __init__(self):
    super().__init__()
    self.level=1
    self.penup()
    self.hideturtle()
    self.goto(-225, 260)
    self.write(f"Level:{self.level}", align=ALIGNMENT, font=FONT)
      
  def update_score(self):
    self.clear()
    self.level +=1
    self.write(f"Level:{self.level}", align=ALIGNMENT, font=FONT)
    
  def game_over(self):
    self.clear()
    self.goto(0, 0)
    self.write(f"Game Over\n", align=ALIGNMENT, font=FONT)

  




