from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import sqlite3
from tkinter import messagebox
import random


main = Tk()
main.title("Account")

# define font
myFont = font.Font(family='Arial', size=20)

labelTop = Label(main, text="Task List")
labelTop['font'] = myFont
labelTop.pack()
def AccountID():
    global AccoID

    c.execute('SELECT ID FROM accounts where username = ?', (username.get(),))
    for AccoID in c:
        AccoID = int(AccoID[0])
        

    #if c.fetchone():
    #    print('Found')
    #    accid = c.fetchone()
    #    print(accid)
    #else:
    #    print('Not found')



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


def login():
    with sqlite3.connect('data.db') as db:
        c = db.cursor()
    
    find_user=("SELECT * FROM accounts where username=? and password = ?")
    c.execute(find_user,[(username.get()), (password.get())])
    result = c.fetchall()
    if result:
        AccountID()
        IN = Label(log, text="You are in!", fg="green")
        IN.pack()
        tasks()
        IN.after(3000, IN.destroy)
    else:
        OUT = Label(log, text="The account does not exist.", fg="red")
        OUT.pack()
        OUT.after(3000, OUT.destroy)

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

    Button(log, text="Log In", command=login,).pack(pady=7)
    Button(log, text="Accounts", command=acco).pack()

openWindowButton = Button(main, text="Log In", command=login_ui, width=15, font="Arial 20")
openWindowButton['font'] = myFont
openWindowButton.pack(padx=5)

with sqlite3.connect('data.db') as db:
    c = db.cursor()


AccTable = '''CREATE TABLE if not exists accounts(
        ID integer PRIMARY KEY,
        username text not null,
        password text not null
        )'''

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

def singup():
    print(n_username.get(),"\n",n_password.get())
    with sqlite3.connect('data.db') as db:
        c = db.cursor()
    
    find_user=("SELECT * FROM accounts where username=?")
    c.execute(find_user,[(n_username.get())])
    if c.fetchall():
        messagebox.showinfo('user','already available')
        print("error")
    else:
        print("Success")
        
        c.execute("INSERT INTO accounts (username, password) VALUES (:username, :password)",
            {
                'username' : n_username.get(),
                'password' : n_password.get()
            }
        )
        
        db.commit()
        db.close()
        #insert = 'INSERT INTO accounts(username, password)values(?, ?)'
        
        #c1.execute(insert,[(n_username.get()),(n_password.get())])
        #try:
        #    with sqlite3.connect('data.db') as db:
        #        c = db.cursor()
             
        #    c.execute("create table user if not exists user(username text not null, primary key,password text not null)")
        #    db.commit()
        #    db.close()
        #    db1.commit()
        #except:
        #    print("not processed")

def signup_ui():
    global n_username
    global n_password
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

openWindowButton = Button(main, text="Sing Up", command=signup_ui, width=15, font="Arial 20")
openWindowButton['font'] = myFont
openWindowButton.pack(pady=7, padx=5)

def tasks():

    global tasktext
    global task
    task = Toplevel()
    tasktext = StringVar()

    task.geometry('400x300')
    task.title("Tasks")

    Button(task, text="Edit", command=edit).grid(row=1)
    Label(task, text="-TASK NAME").grid(row=4, columnspan=6)
    Label(task, text="TASK ENTRY").grid(row=5, columnspan=6)
    Button(task, text="show id", command=AccountID).grid(row=6, column=7)
    
def edit():
    Button(task, text="Save", command=SaveTask).grid(row=1, column=1)
    Button(task, text="Delete").grid(row=1, column=2)
    Button(task, text="Add Task", command=NewTask).grid(row=1, column=3)

def NewTask():
    global taskname
    global textentry
    taskname = StringVar()
    textentry = StringVar()
    
    Label(task, text="Task Name:", pady=3).grid(row=2, columnspan=4)
    Entry(task, width=25, textvariable=taskname).grid(row=2, column=4)
    Label(task, text="Task Entry:").grid(row=3, columnspan=4)
    textentry = Text(task, width=25, height=4)
    textentry.grid(row=3, column=4)
    
def SaveTask():
        
        c.execute("INSERT INTO tasks (taskname, task, acctask) VALUES (:taskname, :task, :acctask)",
        {
            'taskname' : taskname.get(),
            'task' : textentry.get(1.0, END),
            'acctask' : AccoID
        }
    )
        print("Saved!")


main.mainloop()
