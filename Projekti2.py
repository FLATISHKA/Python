from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')


def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)


def add_item():
    if taskname_text.get() == '' or task_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(taskname_text.get(), task_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (taskname_text.get(), task_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        taskname_entry.delete(0, END)
        taskname_entry.insert(END, selected_item[1])
        task_entry.delete(0, END)
        task_entry.insert(END, selected_item[2])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], taskname_text.get(), task_text.get())
    populate_list()


def clear_text():
    taskname_entry.delete(0, END)
    task_entry.delete(0, END)


# Create window object
task = Tk()

# Parts
taskname_text = StringVar()
taskname_label = Label(task, text='Task:', font=('bold', 14), pady=20)
taskname_label.grid(row=0, column=0, sticky=W)
taskname_entry = Entry(task, textvariable=taskname_text)
taskname_entry.grid(row=0, column=1)
# Customer
task_text = StringVar()
task_label = Label(task, text='Text:', font=('bold', 14))
task_label.grid(row=0, column=2, sticky=W)
task_entry = Entry(task, textvariable=task_text)
task_entry.grid(row=0, column=3)
# Parts List (Listbox)
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

task.title('TASKSSSSS')
task.geometry('500x350')

# Populate data
populate_list()

# Start program
task.mainloop()

