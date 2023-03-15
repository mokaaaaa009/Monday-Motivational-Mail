from turtle import *
import heroes
import random

myScreen = Screen()

turtlesColor=["blue","orange","purple","red","green","grey","brown","gold"]
coordinates=[190,140,90,40,-10,-60,-110,-160]
def turtlesSetup(leo,x,y):
  leo.penup()
  leo.goto(x,y)
 


myScreen.setup(width=600,height=400)
turtleNames=["leo","michael","don","raph","oogway","browser","speed","crush"]
winnerBet=myScreen.textinput("Winner Bet","Please Enter your betting:leo,michael,don,raph,oogway,browser,speed,crush")
if winnerBet == "leo":
  userbet=0
elif winnerBet == "michael":
  userbet=1
elif winnerBet == "don":
  userbet=2
elif winnerBet == "raph":
  userbet=3
elif winnerBet == "oogway":
  userbet=4
elif winnerBet == "browser":
  userbet=5
elif winnerBet == "speed":
  userbet=6
else :
  userbet=7     

racers=[]
for i in range(0,8):
  leo = Turtle(shape="turtle")
  leo.color(turtlesColor[i])
  leo.speed('fast')
  
  if i == userbet:
    leo.shapesize(outline=4)
  turtlesSetup(leo,-290,coordinates[i])
  racers.append(leo)
flage=True
while(flage):
  for i in range(0,8):
    step=random.randint(1,20)
    racers[i].forward(step)
    if racers[i].xcor() >290:
      flage=False
      if i == userbet:
        racers[i].goto(0,0)    
        racers[i].setheading(90)
        racers[i].write("We Won !!!",True,align="center",font=("Consolas",20))
        racers[i].goto(0,40)
      else:
        racers[i].goto(0,0)    
        racers[i].setheading(90)

        racers[i].write("You Lose !!! "+turtleNames[i]+" Won",True,align="center",font=("Consolas",20))
        racers[i].goto(0,40)
      break




myScreen.exitonclick()