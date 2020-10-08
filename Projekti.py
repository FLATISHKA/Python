# Importing libraries
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import sqlite3
from tkinter import messagebox
import random
# Importing db.py file with shortcut's
from db import Database

# Main window
main = Tk()
main.title("Account")

# define font
myFont = font.Font(family='Arial', size=20)

labelTop = Label(main, text="Task List")
labelTop['font'] = myFont
labelTop.pack()
# Getting Accout ID from Accounts table
def AccountID():
    global AccoID

    c.execute('SELECT ID FROM accounts where username = ?', (username.get(),))
    for AccoID in c:
        AccoID = int(AccoID[0])
# Printing all Accounts from accouts table
def acco():
    conn = sqlite3.connect('data.db')

    c = conn.cursor()

    c.execute("SELECT * FROM accounts")
    records=c.fetchall()

    print_records = ""

    for record in records:
        print_records += str(record[0]) + " \t " + str(record[1]) + " \t " + str(record[2]) + "\n"

    print(print_records)

    conn.commit()
    conn.close()
# Printing all tasks from tasks table
def taskprint():
    conn = sqlite3.connect('data.db')

    c = conn.cursor()

    c.execute("SELECT * FROM tasks")
    records=c.fetchall()

    print_records = ""

    for record in records:
        print_records += str(record[0]) + " \t " + str(record[1]) + " \t " + str(record[2]) + "\n"

    print(print_records)

    conn.commit()
    conn.close()

# Login
def login():
    with sqlite3.connect('data.db') as db:
        c = db.cursor()
    # Checks if account already exist, and if not it opens a task window
    find_user=("SELECT * FROM accounts where username=? and password = ?")
    c.execute(find_user,[(username.get()), (password.get())])
    result = c.fetchall()
    if result:
        AccountID()
        TaskWindow()
        IN = Label(log, text="You are in!", fg="green")
        IN.pack()
        IN.after(3000, IN.destroy)
    else:
        OUT = Label(log, text="The account does not exist.", fg="red")
        OUT.pack()
        OUT.after(3000, OUT.destroy)
# Login window
def login_ui():
    global username
    global password
    global log

    log = Toplevel()
    log.geometry('300x200')
    log.title("LogIn Form")
    username = StringVar()
    password = StringVar()

    label_username = Label(log, text="Username", font="Arial 15")
    label_username.pack()
    entry_username = Entry(log, textvariable=username, width = 25)
    entry_username.pack()

    label_username= Label(log, text="Password", font="Arial 15")
    label_username.pack()
    entry_password = Entry(log, textvariable=password, width = 25, show="*")
    entry_password.pack()
    # Login Buttons
    Button(log, text="Log In", command=login,).pack(pady=7)
    Button(log, text="Accounts", command=acco, state=DISABLED).pack()
    Button(log, text="Tasks", command=taskprint, state=DISABLED).pack()
# Main window login button
openWindowButton = Button(main, text="Log In", command=login_ui, width=15, font="Arial 20")
openWindowButton['font'] = myFont
openWindowButton.pack(padx=5)
# Connects SQL file
with sqlite3.connect('data.db') as db:
    c = db.cursor()

#Creating Accounts table
AccTable = '''CREATE TABLE if not exists accounts(
        ID integer PRIMARY KEY,
        username text not null,
        password text not null
        )'''
#creating Tasks table
TaskTable = '''CREATE TABLE if not exists tasks (
        acctask integer NOT NULL,
        taskname varchar(20),
        task varchar(100),
        FOREIGN KEY (acctask)
        REFERENCES accounts(ID)
        )'''

c.execute(AccTable)
c.execute(TaskTable)
db.commit
# Singup
def singup():
    print(n_username.get(),"\n",n_password.get())
    with sqlite3.connect('data.db') as db:
        c = db.cursor()
    # Checks if account already exist and if not it creates a new one
    find_user=("SELECT * FROM accounts where username=?")
    c.execute(find_user,[(n_username.get())])
    if c.fetchall():
        OUT=Label(reg, text="Account already exist", fg="red")
        OUT.pack()
        OUT.after(3000, OUT.destroy)
        print("error")
    else:
        IN=Label(reg, text="Account created", fg="green")
        IN.pack()
        IN.after(3000, IN.destroy)
        print("Success")
        # Inserting singup entry username and password into accounts table
        c.execute("INSERT INTO accounts (username, password) VALUES (:username, :password)",
            {
                'username' : n_username.get(),
                'password' : n_password.get()
            }
        )
        
        db.commit()
        db.close()
# Singup window
def signup_ui():
    global n_username
    global n_password
    global reg

    reg = Toplevel()
    reg.geometry('300x200')
    reg.title("SignUp Form")
    n_username = StringVar()
    n_password = StringVar()

    label_username = Label(reg, text="Username", font="Arial 15")
    label_username.pack()
    entry_username = Entry(reg, textvariable=n_username, width = 25)
    entry_username.pack()
 
    label_password = Label(reg, text="Password", font="Arial 15")
    label_password.pack()
    entry_password = Entry(reg, textvariable=n_password, width = 25)
    entry_password.pack()

    Button(reg, text="Sign Up", command= singup).pack(pady=7)

# Main screen singup button
openWindowButton = Button(main, text="Sing Up", command=signup_ui, width=15, font="Arial 20")
openWindowButton['font'] = myFont
openWindowButton.pack(pady=7, padx=5)

##############################   Task window and commands ###################################
db = Database('data.db')

# Accounts all Tasks
def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch(AccoID):
        parts_list.insert(END, row)

# Adds items that was writed in entry
def add_item():
    # If entry is clear it asks you to include all fields
    if taskname_text.get() == '' or task_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(AccoID, taskname_text.get(), task_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (taskname_text.get(), task_text.get()))
    clear_text()
    populate_list()

# Selected item
def select_item(event):
    try:
        global selected_item
        global TaskSelect
        
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        taskname_entry.delete(0, END)
        taskname_entry.insert(END, selected_item[1])
        task_entry.delete(0, END)
        task_entry.insert(END, selected_item[2])
        TaskSelect = selected_item[1]
    except IndexError:
        pass

# Removes selected item
def remove_item():
    db.remove(TaskSelect)
    clear_text()
    populate_list()

# Updates selected item
def update_item():
    db.update(TaskSelect, taskname_text.get(), task_text.get())
    populate_list()

# Clears all entrys
def clear_text():
    taskname_entry.delete(0, END)
    task_entry.delete(0, END)

# Task Window
def TaskWindow():
    task = Toplevel()
    task.title('Tasks')
    task.geometry('700x350')
    global taskname_entry
    global taskname_text
    global task_entry
    global task_text 
    global parts_list

    # Task
    taskname_text = StringVar()
    taskname_label = Label(task, text='Task:', font=('bold', 14), pady=20)
    taskname_label.grid(row=0, column=0, sticky=W)
    taskname_entry = Entry(task, textvariable=taskname_text)
    taskname_entry.grid(row=0, column=1)
    # Task text
    task_text = StringVar()
    task_label = Label(task, text='Text:', font=('bold', 14))
    task_label.grid(row=0, column=2, sticky=W)
    task_entry = Entry(task, textvariable=task_text)
    task_entry.grid(row=0, column=3)
    # Task List (Listbox)
    parts_list = Listbox(task, height=8, width=50, border=0)
    parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
    # Create scrollbar
    scrollbar = Scrollbar(task)
    scrollbar.grid(row=3, column=3)
    # Set scroll to listbox
    parts_list.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=parts_list.yview)
    # Bind select
    parts_list.bind('<<ListboxSelect>>', select_item)

    # Buttons
    add_btn = Button(task, text='Add Part', width=12, command=add_item)
    add_btn.grid(row=2, column=0, pady=20)

    remove_btn = Button(task, text='Remove Part', width=12, command=remove_item)
    remove_btn.grid(row=2, column=1)

    update_btn = Button(task, text='Update Part', width=12, command=update_item)
    update_btn.grid(row=2, column=2)

    clear_btn = Button(task, text='Clear Input', width=12, command=clear_text)
    clear_btn.grid(row=2, column=3)


    # Populate data
    populate_list()

# Start program
main.mainloop()
"""
.             ##########         ##########
.           ##############     ##############
.          ###################################
.          ###################################
.          ###################################
.           ################################
.             ############################
.               #########################
.                 #####################
.                    ###############
.                      ###########
.                         #####
.
.                Kiitos Mira Opetuksesta!
"""