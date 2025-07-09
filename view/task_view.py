import customtkinter
from tkinter import messagebox
class TaskView:
    # MAIN MENU
    def task_menu(self):
        # Creates a Window, sets a title and a size
        self.__main_window = customtkinter.CTk()
        self.__main_window.title("Task Tracker")
        self.__main_window.geometry("400x400")
        
        # Set selected option to none
        self.__selected_option = None
        
        # Define the title 
        title = customtkinter.CTkLabel(self.__main_window, text="Task Menu", font=("Arial", 16))
        title.pack(pady=15)
        
        # A list of tuples to define the avaiable options on the menu
        buttons = [
            ("Add Task", 1),
            ("List Tasks", 2)
        ]
        
        
        # A for loop to create each button, and the lambda function returns the valor to the button that was selected
        for text, valor in buttons:
            button = customtkinter.CTkButton(self.__main_window, text=text, command=lambda v=valor: self.__select(v))
            button.pack(pady=15)
            
        self.__main_window.mainloop()
        self.__main_window.destroy()

        return self.__selected_option
    
    # Auxiliary function that return the selected option on the lambda function
    def __select(self, valor):
        self.__selected_option = valor
        self.__main_window.quit()
    # FUNCTIONS RELATED TO THE MAIN MENU END HERE
    
    
    # ADD TASK
    def add_task(self):
        # Creates a window to add task
        self.__add_window = customtkinter.CTk()
        self.__add_window.title("Add task description")
        self.__add_window.geometry("400x400")
        
        title = customtkinter.CTkLabel(self.__add_window, text="Add Task Menu", font=("Arial", 16))
        title.pack(pady=10)
        
        # CTkEntry creates an input field
        self.__description = customtkinter.CTkEntry(self.__add_window, placeholder_text='task description')
        self.__description.pack(pady=15, padx=10)
        
        # Set the task data to None
        self.__task_data = None
        
        # Creates a confirmation button
        confirm_button = customtkinter.CTkButton(self.__add_window, text='Confirm', command=self.__confirm)
        confirm_button.pack(pady=15)
        
        self.__add_window.mainloop()
        self.__add_window.destroy()
        
        # return a dict with the description
        return self.__task_data    

    def __confirm(self):
        description = self.__description.get()
        
        self.__task_data = {
            "description": description
        }
        
        self.__add_window.quit()
    # FUNCTIONS RELATED TO ADD TASK END HERE
        
    
    # SHOW TASKS 
    def show_tasks(self, tasks):
        # Create the window
        self.__show_tasks_window = customtkinter.CTk()
        self.__show_tasks_window.title("All tasks")
        self.__show_tasks_window.geometry("600x400")
        
        title = customtkinter.CTkLabel(self.__show_tasks_window, text="Registered Tasks", font=('Arial', 14))
        title.pack(pady=20)
               
        # if the task list received is empty create a label that shows "No tasks"
        if not tasks:
            message = customtkinter.CTkLabel(self.__show_tasks_window, text="No Tasks")
            message.pack(pady=10)
            
        # If the task is not empty creates a Scrollable Frame and show the tasks
        else:
            frame = customtkinter.CTkScrollableFrame(self.__show_tasks_window, width=350, height=300)
            frame.pack(pady=20)
            
            for task in tasks:
                text = (
                    f"Description: {task.description}\n"
                    f"Status: {task.status}\n"
                    f"Created: {task.created.strftime('%d/%m/%Y %H:%M')}\n"
                    f"Completed: {task.completed}\n"
                    "----------------------------------"
                )
                label = customtkinter.CTkLabel(frame, text=text, justify="left", anchor='w')
                label.pack(padx=10, pady=5, fill='x')
        
        # Button to return to list tasks menu
        button = customtkinter.CTkButton(self.__show_tasks_window, text="Return", command=self.__show_tasks_window.quit)
        button.pack(pady=15)
        
        self.__show_tasks_window.mainloop()
        self.__show_tasks_window.destroy()
    # END OF SHOW TASKS
    
    def update_tasks(self):
        pass
        
    
    
    # FUNCTION TO SHOW MESSAGES ON THE SCREEN
    def show_message(self, message: str):
        messagebox.showinfo("Information", message)