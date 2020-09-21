from tkinter import *
from tkinter import messagebox
import tkinter.font as font

main = Tk()
main.title("Account")

# define font
myFont = font.Font(family='Arial', size=20)

labelTop = Label(main, text="Valitse käyttäjä")
labelTop['font'] = myFont
labelTop.grid(row=0, column=2, columnspan=2, pady=5)

options=[
    "First",
    "Second",
    "Third",
    "Fourth",
    "Fifth",
]

selectItem = StringVar()
selectItem.set(options[0])

def show():
    myLabel=Label(main, text=selectItem.get().pack)

drop = OptionMenu(main, selectItem, *options)
drop.config(width=7)
drop['font'] = myFont
drop.grid(row=1, column=2, padx= 3)

myButton = Button(main, text="    Hae    ", command=show)
myButton['font'] = myFont
myButton.grid(row=1, column=3, padx=3)

def register():
    global reg

    reg = Toplevel()
    reg.geometry('300x250')
    reg.title("Register")

    Label(reg, text="Username", font="Arial 15").pack()
    Username = Entry(reg, width = 25)
    Username.pack()

    Label(reg, text="Password", font="Arial 15").pack()
    Password = Entry(reg, width = 25, show="*")
    Password.pack()
    

openWindowButton = Button(main, text="Register", command=register, width=15, font="Arial 20")
openWindowButton['font'] = myFont
openWindowButton.grid(row=4, column=2, columnspan= 2, padx=10, pady=10)

main.mainloop()
