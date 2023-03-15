from tkinter import *
from tkinter import messagebox
import random
import json
import pandas as pd

#-----------------Constant--------------------------
BACKGROUND_COLOR = "#B1DDC6"
ANSWERFONT=("arial",30)
FONT=("arial",300)

def flipCard():
  myCanvas.itemconfig(card_Image,image=card_Image_back)
  hiraganaOn=kanji["hirganaOn"]
  hiraganaKon=kanji["hiraganaKon"]
  Onyumi=kanji["Onyumi"]
  Meaning=kanji["Meaning"]
  myCanvas.itemconfig(kanjiWord,text=f"Hiragana Onyumi = {hiraganaOn} \nRomanji={Onyumi}\nHiragana Kunyomi = {hiraganaKon} \nMeaning = {Meaning}",font=ANSWERFONT,fill="white")
  



#------------------Setup Window----------------------
myWindow=Tk()
myWindow.title("N5 Japanese Kanji")
myWindow.config(padx=50,pady=50,background=BACKGROUND_COLOR)
flip_Timer=myWindow.after(3000,flipCard)
#------------------Reading from Files------------------------
newKanji=[]
try:
  myKanji=pd.read_csv("kanji_to_learn.csv",encoding="shift-jis")
except FileNotFoundError:
  myKanji = pd.read_csv("kanji.csv",encoding="shift-jis")
  newKanji=myKanji.to_dict(orient="records")
else:
  newKanji=myKanji.to_dict(orient="records")
  



def pickLetter():
  global kanji,flip_Timer,newKanji
  kanji=random.choice(newKanji)
  myWindow.after_cancel(flip_Timer)
  question=kanji["kanji"]
  myCanvas.itemconfig(kanjiWord,text=question,font=FONT,fill="black")
  myCanvas.itemconfig(card_Image,image=card_Image_front)
  flip_Timer= myWindow.after(3000,flipCard)


def isknown():
  newKanji.remove(kanji)
  print(len(newKanji))
  data = pd.DataFrame(newKanji)
  data.to_csv("Kanji_to_Learn.csv",index=False,encoding="shift-jis")
  pickLetter()
  

def retry_Question():
  global flip_Timer
  myWindow.after_cancel(flip_Timer)
  question=kanji["kanji"]
  myCanvas.itemconfig(kanjiWord,text=question,font=FONT,fill="black")
  myCanvas.itemconfig(card_Image,image=card_Image_front)
  flip_Timer= myWindow.after(3000,flipCard)


#image
right_image=PhotoImage(file="right.png")
wrong_image=PhotoImage(file="wrong.png")
card_Image_front = PhotoImage(file="card_front.png")
card_Image_back=PhotoImage(file="card_back.png")
restart_image=PhotoImage(file="restart.png")



#------------------Steup Canvas---------------------
myCanvas=Canvas(width=1000,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)

card_Image=myCanvas.create_image(500,263,image=card_Image_front)
kanjiWord=myCanvas.create_text(500,200,font=FONT)

myCanvas.grid(row=0,column=0,columnspan=3,padx=5)


#--------------------Button-------------------------
wrong_Btn=Button(image=wrong_image,width=100,height=99,padx=50,command=pickLetter)
wrong_Btn.grid(row=1,column=0)
wrong_Btn.config(borderwidth=0,highlightthickness=0)

right_Btn=Button(image=right_image,width=100,height=100,command=isknown)
right_Btn.config(borderwidth=0,highlightthickness=0)
right_Btn.grid(row=1,column=2)

restart_Btn=Button(image=restart_image,width=100,height=100,bg=BACKGROUND_COLOR,command=retry_Question)
restart_Btn.config(borderwidth=0,highlightthickness=0)
restart_Btn.grid(row=1,column=1)
pickLetter()




myWindow.mainloop()


