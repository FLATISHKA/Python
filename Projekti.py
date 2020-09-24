from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import sqlite3
from tkinter import messagebox

main = Tk()
main.title("Account")

# define font
myFont = font.Font(family='Arial', size=20)

labelTop = Label(main, text=":D")
labelTop['font'] = myFont
labelTop.pack()

def query():
    conn = sqlite3.connect('data.db')

    c = conn.cursor()

    c.execute("SELECT * FROM accounts")
    records=c.fetchall()

    print_records = ""

    for record in records:
        print_records += str(record[0]) + " \t " + str(record[1]) + "\n"

    print(print_records)

    conn.commit()
    conn.close()


def login():
    with sqlite3.connect('data.db') as db:
        c = db.cursor()
    
    find_user=("SELECT * FROM accounts where username=? and password = ?")
    c1.execute(find_user,[(username.get()), (password.get())])
    result = c.fetchall()
    if result:
        messagebox.showinfo('Success', 'you are in!')
    else:
        messagebox.showinfo('Error', 'the account does not exist.')

def login_ui():
    global username
    global password

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
    Button(log, text="Accounts", command=query).pack()

openWindowButton = Button(main, text="Log In", command=login_ui, width=15, font="Arial 20")
openWindowButton['font'] = myFont
openWindowButton.pack(padx=5)

with sqlite3.connect('data.db') as db1:
    c1 = db1.cursor()

c1.execute("create table if not exists accounts(username text not null, password text not null)")

def singup():
    print(n_username.get(),"\n",n_password.get())
    with sqlite3.connect('data.db') as db1:
        c1 = db1.cursor()
    
    find_user=("SELECT * FROM accounts where username=?")
    c1.execute(find_user,[(n_username.get())])
    if c1.fetchall():
        messagebox.showinfo('user','already available')
        print("error")
    else:
        print("Success")

        c1.execute("INSERT INTO accounts VALUES (:username, :password)",
            {
                'username' : n_username.get(),
                'password' : n_password.get()
            }
        )
        c1.commit()

        c1.close()
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



main.mainloop()
