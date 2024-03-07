import tkinter as tk
import customtkinter as ctk 
"""
    manage a task in a customtkinter
    
    fonction to use :
                    add_task():
                        add to list a task to write
                    remove_task():
                        remove to list a task to select 
"""

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app =  ctk.CTk()
app.geometry("400x240")
app.title("to do list")

task = []

def add_task():
    """ module add_task

        this module add a task a list 
        if a task is empty not add a list 
        else add a list 
        ############################
        
    """
    task_text = task_user.get()
    
    if task_text:
        task.append(task_text)
        task_user.delete(0, ctk.END)
        task_list.insert(ctk.END, task_text)
        

def remove_task():
    """ module remove_task

        this module remove a curent task a list 
        if a task is empty not reove a list 
        else remove a list the taask selected
        ############################
        
    """
    check_index = task_list.curselection()
    if check_index:
        task_index = check_index[0]
        del task[task_index]
        task_list.delete(task_index)


user_label = ctk.CTkLabel(app,text="Enter your Task :")
user_label.grid(row = 0,column=0)
task_user = ctk.CTkEntry(app)
task_user.grid(row = 0,column=1)

button_add = ctk.CTkButton(app,text="Button Add" ,command= add_task)
button_add.grid(row = 1,column=0)

button_remove = ctk.CTkButton(app,text="Button Remove",command = remove_task)
button_remove.grid(row = 1,column=1,padx=10,pady=10)

task_list = ctk.Listbox(app,width=50)
task_list.grid(row=0,column=2)

app.mainloop()


