import tkinter as tk

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestionnaire de tâches")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=20)
        
        self.add_button = tk.Button(self.root, text="Ajouter une tâche", command=self.add_task)
        self.add_button.pack(pady=10)
        
        self.task_list = tk.Listbox(self.root, width=50)
        self.task_list.pack(pady=20)
        
        self.remove_button = tk.Button(self.root, text="Supprimer la tâche sélectionnée", command=self.remove_task)
        self.remove_button.pack(pady=10)
        
    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.task_list.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)
            
    def remove_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.task_list.delete(task_index)

root = tk.Tk()
task_manager = TaskManager(root)
root.mainloop()
