from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(column=0,row=0)

#buttons
def action():
    print("do something")

#calls action() when pressed
button = Button(text="click me", command=action)
button.grid(column=2,row=0)


#calls action() when pressed
nbutton = Button(text="click me", command=action)
nbutton.grid(column=1,row=1)



#entries
entry = Entry(width=30)
#add some text to begin with
entry.insert(END, string="some text to begin with.")
entry.grid(column=3,row=2)






window.mainloop()