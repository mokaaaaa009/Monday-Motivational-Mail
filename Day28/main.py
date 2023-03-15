from tkinter import*
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
mainreps=0
minibreakflage=True
longbreakflage=False
timer=None
spinbox=None
#mark="✔"
window=Tk()
window.title("Pomodoro")


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
   global mainreps
   mainreps=0
   window.after_cancel(timer)
   check_Label.config(text="")
   timer_Text.config(text="Timer")
   canvas.itemconfig(countdown_Text,text="00:00")




# ---------------------------- TIMER MECHANISM ------------------------------- # 
def setTimer():
   global mainreps
   #global mark
   mainreps+=1
   global spinbox
   minutes=int(spinbox.get())
   if mainreps%8 ==0:
      #check_Label.config(text="")
      #mark="✔"
      countdown(minutes*60)
      timer_Text.config(text="Long Break",fg=RED)
   elif mainreps%2==0:
      
      #check_Label.config(text=mark)
      #mark+="✔"
      countdown(minutes*60)
      timer_Text.config(text="Short Break",fg=PINK)
   else:
      countdown(minutes*60)
      timer_Text.config(text="Work Time",fg=GREEN)


      
      

  











#   global minibreakflage
  #  if mainreps ==0:
  #   countdown(3)
  #   mainreps+=1
  #   minibreakflage=False
  #  elif mainreps < 4 and minibreakflage == False:
  #   countdown(1)
  #   minibreakflage=True
  #  elif mainreps < 4 and minibreakflage == True:
  #   countdown(3)
  #   mainreps+=1
  #   minibreakflage=False
  #  else:
  #    countdown(2)
  #    mainreps=0  




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(time):
    global timer
    minutes = math.floor(time/60)
    seconds=time % 60
    canvas.itemconfig(countdown_Text,text=f"{minutes:02d}:{seconds:02d}")
    if time>0:    
      timer=window.after(1000,countdown,time-1)
      print(time)
    else:
       #window.lift()
       window.attributes('-topmost',True)
       window.attributes('-topmost',False)  
      #  setTimer()
      #  mark=""
      #  work_session=math.floor(mainreps/2)
      #  for _ in range(work_session):
      #     mark+="✔"
      #  check_Label.config(text=mark)   
      

# ---------------------------- UI SETUP ------------------------------- #


#Read image 
bg=PhotoImage(file="../tomato.png")

#set width and height of canvas that display the image 
canvas=Canvas(width=220 ,height=224,bg=YELLOW,highlightthickness=0)

#upload the image to canvas
canvas.create_image(108,112,image=bg)
#ask User of duration he wants to focus 
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=15, to=240, width=5,increment=5 ,command=spinbox_used)
spinbox.grid(column=1,row=2)
#write the timer in center of image
countdown_Text=canvas.create_text(110,130,text="00:00",font=(FONT_NAME,30,"bold"),fill="white")
canvas.grid(column=1,row=1)
#write Timer word on top of image
timer_Text=Label(text="Timer",font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
timer_Text.grid(column=1,row=0)

#Start Button configuration
start_Button=Button(text="Start",font=(FONT_NAME,12,"bold"),command=setTimer)
start_Button.grid(column=0,row=2)

#Reset Button configuration
reset_Button=Button(text="Reset",font=(FONT_NAME,12,"bold"),command=reset)
reset_Button.grid(column=2,row=2)

window.config(padx=100,pady=50,bg=YELLOW)

check_Label=Label(font=(FONT_NAME,12),fg=GREEN,bg=YELLOW)
check_Label.grid(column=1,row=3)

window.mainloop()
