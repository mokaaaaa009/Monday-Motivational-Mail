import csv
from turtle import*
import turtle
import pandas as pd
from tkinter import messagebox
import time
africa="Africa.gif"
myScreen = Screen()

myScreen.setup(width=600,height=800)
myScreen.addshape(africa)

myCountries=Turtle()
myCountries.shape(africa)
Countries = pd.read_csv(r"C:\Users\Owner\DaysCode100\africawithCoord.csv")
africa=Countries["Countries"].tolist()
ALIGN="center"
FONT=("verdana", 12, "bold")
gameisON=True
timerText=Turtle()
timerText.up()
timerText.hideturtle()
start= time.time()
print(time.time() - start)
already=[]

while len(already)<55:
   ans=myScreen.textinput(title=f"Guess the country{len(already)}/54",prompt="Enter the country name")
   if ans ==None:
    messagebox.showinfo("Surender!!!",message="the rest Countries will be revealed")
    for ans in africa:
      revealer=Turtle()
      revealer.up()
      revealer.hideturtle()  
      revealer.color("Black")
      pos = Countries[Countries.Countries==ans]
      revealer.goto(int(pos.X),int(pos.Y))
      revealer.write(ans,font=FONT,align=ALIGN)
    break   
   elif ans.title() in already:
      messagebox.showinfo("Already Written",message="Country written before")
   elif ans.title() in africa:
      pointer=Turtle()
      pointer.up()
      pointer.hideturtle()  
      pointer.color("white")
      pos = Countries[Countries.Countries == ans.title()]
      already.append(ans)
      pointer.goto(int(pos.X),int(pos.Y))
      pointer.write(ans.title(),font=FONT,align=ALIGN)
   else:
      messagebox.showinfo(message="There's no african country in that name")


     



yp=[]
xp=[]
i=0

myScreen.exitonclick()
