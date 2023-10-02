
import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=40, selectmode=tk.MULTIPLE)
        self.task_listbox.pack()

        clear_button = tk.Button(root, text="Clear All Tasks", command=self.clear_tasks)
        clear_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_indices = self.task_listbox.curselection()
        
        if selected_indices:
            confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to remove the selected tasks?")
            
            if confirmed:
                for index in reversed(selected_indices):
                    del self.tasks[index]
                    self.task_listbox.delete(index)

    def clear_tasks(self):
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
        
        if confirmed:
            self.tasks.clear()
            self.task_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()

# Create an instance of the TodoListApp class
app = TodoListApp(root)

# Start the Tkinter event loop
root.mainloop()