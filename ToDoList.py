'''
ToDoList.py
program a todo list with a GUI using python
'''

import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List App")


# create functions
def add_task():
    task = task_entry.get()
    if task != "":
        listbox_task.insert(tkinter.END, task)
        task_entry.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(
            title="Warning", message="You need to enter a task.")


def delete_task():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(
            title="Warning", message="You need to select a task.")


def save_task():
    task = listbox_task.get(0, listbox_task.size())
    pickle.dump(task, open("task.dat", "wb"))
    tkinter.messagebox.showinfo(
        title="Information", message="Your task has been saved.")


def load_task():
    try:
        task = pickle.load(open("task.dat", "rb"))
        listbox_task.delete(0, tkinter.END)
        for task in task:
            listbox_task.insert(tkinter.END, task)

        tkinter.messagebox.showinfo(
            title="Information", message="Your task has been loaded.")

    except:
        tkinter.messagebox.showwarning(
            title="Warning", message="No previous tasks found.")


# create GUI
frame = tkinter.Frame(root)
frame.pack()

listbox_task = tkinter.Listbox(frame, height=5, width=50)
listbox_task.pack(side=tkinter.LEFT)

scrollbar_task = tkinter.Scrollbar(frame)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

task_entry = tkinter.Entry(root, width=50)
task_entry.pack()

# create buttons
add_task_button = tkinter.Button(
    root, text="Add Task", width=48, command=add_task)
add_task_button.pack()

delete_task_button = tkinter.Button(
    root, text="Delete Task", width=48, command=delete_task)
delete_task_button.pack()

save_task_button = tkinter.Button(
    root, text="Add Task", width=48, command=save_task)
save_task_button.pack()

load_task_button = tkinter.Button(
    root, text="Load Task", width=48, command=load_task)
load_task_button.pack()

root.mainloop()
