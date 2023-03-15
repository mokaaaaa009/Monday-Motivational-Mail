from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list=[random.choice(letters) for char in range(nr_letters)]
    password_list+=[random.choice(symbols) for char in range(nr_symbols)]
    password_list+=[random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_Entry.insert(0, password)
    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website=website_Entry.get()
    email=email_Entry.get()
    password=password_Entry.get()
    if len(website)==0 or len(email)==0 or len(password)==0:
       messagebox.showwarning(title="Missing information", message="Please enter all information")
    else:
      isok=messagebox.askokcancel(title="Confirm Input",message=f"These are the details you insterted Website:{website}\n email: {email}\n password: {password}\n is it ok to save?")
      if isok:
         with open("password.txt","a") as f:
            f.write(f"{website}|{email}|{password}\n")
         website_Entry.delete(0,END)
         password_Entry.delete(0,END)

      
# ---------------------------- UI SETUP ------------------------------- #






#-----------------------Variables ----------------------------------------------------------------
FONT="Courier"

myWindow = Tk()
myWindow.title("Password Manager")
logo=PhotoImage(file="Day29\logo.png")
canvas= Canvas(width=200,height=200)
myWindow.config(padx=30,pady=30)

canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)
#labels
website_Label = Label(text="Website:")
website_Label.grid(row=1,column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)
#Entries
website_Entry = Entry(width=35)
website_Entry.grid(row=1,column=1,columnspan=2)
website_Entry.focus()
email_Entry = Entry(width=35)
email_Entry.grid(row=2,column=1,columnspan=2)
#set default value
email_Entry.insert(0,"abc@hotmail.com")
password_Entry = Entry(width=30)
password_Entry.grid(row=3,column=1)
#buttons
generate_Btn=Button(text="Generate Password",command=generate_password)
generate_Btn.grid(row=3,column=2)

add_Btn=Button(text="Add",width=45 ,command=save)
add_Btn.grid(row=4,column=1,columnspan=2)











myWindow.mainloop()