# task_manager_gui.py

import tkinter as tk
from tkinter import messagebox

class TaskManagerGUI:
    def __init__(self, filename):
        self.tasks = self.load_tasks(filename)
        self.filename = filename
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.task_list = tk.Listbox(self.root, width=40)
        self.task_list.pack(padx=10, pady=10)
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(padx=10, pady=10)
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)
        self.edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(padx=10, pady=10)
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)
        self.complete_button = tk.Button(self.root, text="Mark Task Complete", command=self.mark_task_complete)
        self.complete_button.pack(padx=10, pady=10)
        self.display_tasks()

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks = [line.strip().split(',') for line in file.readlines()]
                return [{'description': task[0], 'complete': task[1] == 'True'} for task in tasks]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task['description']},{task['complete']}\n")

    def add_task(self):
        description = self.entry.get()
        self.tasks.append({'description': description, 'complete': False})
        self.save_tasks()
        self.display_tasks()
        self.entry.delete(0, tk.END)

    def edit_task(self):
        index = self.task_list.curselection()[0]
        description = self.entry.get()
        self.tasks[index]['description'] = description
        self.save_tasks()
        self.display_tasks()
        self.entry.delete(0, tk.END)

    def delete_task(self):
        index = self.task_list.curselection()[0]
        del self.tasks[index]
        self.save_tasks()
        self.display_tasks()

    def mark_task_complete(self):
        index = self.task_list.curselection()[0]
        self.tasks[index]['complete'] = True
        self.save_tasks()
        self.display_tasks()

    def display_tasks(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            status = 'Complete' if task['complete'] else 'Incomplete'
            self.task_list.insert(tk.END, f"{task['description']} - {status}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = TaskManagerGUI('tasks.txt')
    gui.run()