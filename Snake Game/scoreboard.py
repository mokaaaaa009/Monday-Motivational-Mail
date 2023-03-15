import turtle
ALIGNMENT="center"
FONT=("Courier", 12, "normal")

class Scoreboard (turtle.Turtle):
  
  def __init__(self):
    super().__init__()
    with open("data.txt",mode="r") as dscore:
      self.highScore=int(dscore.read())    
    self.score=0
    self.penup()
    self.hideturtle()
    self.goto(0, 280)
    self.write(f"Score:{self.score} High Score:{self.highScore}", align=ALIGNMENT, font=FONT)  
 
  def update_score(self):
    self.score+=1
    self.clear()
    self.write(f"Score:{self.score} High Score:{self.highScore}", align=ALIGNMENT, font=FONT)
 
  def reset(self):
    if self.score > self.highScore:
      self.highScore=self.score
      with open("data.txt", "w") as dscore:
        dscore.write(str(self.highScore))
    self.score=0
    self.clear()
    self.write(f"Score:{self.score} High Score:{self.highScore}", align=ALIGNMENT, font=FONT)

   
     

  




