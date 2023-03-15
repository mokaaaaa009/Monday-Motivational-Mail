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
country=Countries["Countries"].tolist()
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
   ans=myScreen.textinput(title=f"Guess the country{len(already)}/54",prompt="Enter the country name").title()
   timerText.goto(-290,380)
   timerText.clear()
   timerText.write(time.time()-start,font=FONT,align=ALIGN)
   if ans in already:
      messagebox.showinfo("Already Written",message="Country written before")
   elif ans in country:
      pointer=Turtle()
      pointer.up()
      pointer.hideturtle()  
      pointer.color("white")
      pos = Countries[Countries.Countries == ans]
      already.append(ans)
      pointer.goto(int(pos.X),int(pos.Y))
      pointer.write(ans,font=FONT,align=ALIGN)
   else:
      messagebox.showinfo(message="There's no african country in that name")

     



yp=[]
xp=[]
i=0
# for i in range(len(country)):
#   pointer=Turtle()
#   pointer.up()  
#   pointer.color("white")
#   pointer.goto(Countries.X[i],Countries.Y[i])
#   pointer.write(country[i])
#def get_mouse_click_coor(x, y):
 # print(x,y)

      # pointer=Turtle()
      # pointer.up()  
      # pointer.color("white")
#      xp.append(x)
#      yp.append(y)
#      global i
#      pointer.goto(x,y) 
#      pointer.write(country[i],FONT,ALIGN)
#      i+=1
#      if len(xp) ==54:
#        Countries.X=xp
#        Countries.Y=yp
#        print(xp)
#        print(yp)
#        Countries.to_csv("africawithcoord")
       
       
#myScreen.onscreenclick(get_mouse_click_coor)
#myScreen.mainloop()
#print(Countries)

myScreen.exitonclick()
