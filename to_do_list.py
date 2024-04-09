from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("To Do List Application")
root.geometry("400x450")
root.resizable(0,0)
root.config(bg="#9CAFAA")

def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(END, task)
        entry.delete(0,END)
        save_task()
    else:
        messagebox.showwarning("Warning","Please enter a task !")

def remove_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
        save_task()
    else:
        messagebox.showwarning('Warning',"Choose a task to delete")

def save_task():
    with open("tasks.txt","w") as f:
        tasks =task_listbox.get(0,END)
        for task in tasks:
            f.write(task + "\n")

def load_task():
    try:
        with open("tasks.txt","r") as f:
            tasks = f.readlines()
            for task in tasks:
                task_listbox.insert(0,task.strip())
    except FileNotFoundError:
        messagebox.showwarning("Warning","Cannot load tasks.")


label = Label(root, text="Enter the task to add", font=("Arial",13))
label.grid(column=0,row=0,padx=5,pady=10,sticky="W")

entry = Entry(root, width=30, font=("Arial",15))
entry.grid(column=0,row=1,padx=5,pady=5,sticky="W")

btn_add = Button(root, text="Add Task",bg="#FF5BAE", font=("Arial",13), command=add_task)
btn_add.grid(column=0,row=2,padx=5,pady=1,sticky="W")

btn_remove = Button(root, text="Remove Task",bg="#9F70FD", font=("Arial",13),command=remove_task)
btn_remove.grid(column=0,row=3,sticky="W",padx=0,pady=5)

list_label = Label(root,text="List of Tasks", font=("Arial",12),bg="#9ADE7B")
list_label.grid(column=0,row=4,padx=5,pady=5,sticky="W")

task_listbox = Listbox(root,width=50)
task_listbox.grid(column=0,row=5,sticky="W",padx=10,pady=5)

load_task()

root.mainloop()