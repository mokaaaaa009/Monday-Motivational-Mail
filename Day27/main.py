from tkinter import*

def add(*nums):
    i=0
    for j in nums:
        i+=j
    return i
def calculate():
    mile=entryMiles.get()
    km =float(mile)*1.609344
    resultLabel.config(text=str(km))
    
window = Tk()
window.title("Let's go")
window.config(padx=10,pady=10)
window.minsize(width=200, height=100)

entryMiles= Entry(width=20)
entryMiles.grid(column=1,row=0)

label1=Label(text="Miles")
label1.grid(column=2,row=0)

label2 = Label(text="equals to")
label2.grid(column=0,row=1)

resultLabel = Label(text="")
resultLabel.grid(column=1,row=1)

label3 = Label(text="Km")
label3.grid(column=2,row=1)

actionButton = Button(text="Calculate",command=calculate)
actionButton.grid(column=1,row=2)





window.mainloop()