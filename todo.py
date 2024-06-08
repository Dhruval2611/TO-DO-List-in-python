import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.configure(bg="#003C43")
        
        self.tasks = []
        
        self.create_widgets()
    
    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="#003C43")
        self.frame.pack(pady=20, padx=20, fill=tk.X)
        
        self.task_entry = tk.Entry(self.frame, font=('Times New Roman', 18, 'bold'), bd=0, bg="#77B0AA", fg="#003C43")
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=5)
        
        self.add_task_btn = tk.Button(self.frame, text="Add Task", command=self.add_task, bg="#135D66", fg="#E3FEF7", font=('Times New Roman', 18, 'bold'), borderwidth=0)
        self.add_task_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.tasks_listbox = tk.Listbox(self.root, height=15, width=60, bg="#77B0AA", fg="#003C43", font=('Times New Roman', 18, 'bold'), bd=0, highlightthickness=0, selectbackground="#135D66", selectforeground="#E3FEF7")
        self.tasks_listbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        self.buttons_frame = tk.Frame(self.root, bg="#003C43")
        self.buttons_frame.pack(pady=10, padx=20, fill=tk.X)
        
        self.delete_task_btn = tk.Button(self.buttons_frame, text="Delete Task", command=self.delete_task, bg="#135D66", fg="#E3FEF7", font=('Times New Roman', 18, 'bold'), borderwidth=0)
        self.delete_task_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.clear_tasks_btn = tk.Button(self.buttons_frame, text="Clear To-Do", command=self.clear_tasks, bg="#135D66", fg="#E3FEF7", font=('Times New Roman', 18, 'bold'), borderwidth=0)
        self.clear_tasks_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.exit_btn = tk.Button(self.buttons_frame, text="Exit", command=self.root.quit, bg="#135D66", fg="#E3FEF7", font=('Times New Roman', 18, 'bold'), borderwidth=0)
        self.exit_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")
    
    def clear_tasks(self):
        self.tasks.clear()
        self.update_task_list()
    
    def update_task_list(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

