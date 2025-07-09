from dao.task_dao import TaskDAO
from model.task import Task
from view.task_view import TaskView
from datetime import datetime

class TaskController:
    def __init__(self) -> None:
        self.__task_view = TaskView()
        self.__task_dao = TaskDAO()
        
        
    def initialize(self):
        while True:
            option = self.__task_view.task_menu()
            match option:
                case 1:
                    self.add_task()
                case 2:
                    self.show_all_tasks()
                case _:
                    self.__task_view.show_message("Invalid option")

    
    def add_task(self):
        data = self.__task_view.add_task()
        if data is None:
            self.__task_view.show_message("Task register cancelled")
            return
        
        task = Task(
            description=data["description"],
            status="To do",
            creation_date=datetime.now()
        )
        
        self.__task_dao.add(task)
        self.__task_view.show_message("Task registered successfully")
    
    
    def show_all_tasks(self):
        tasks_to_list = self.__task_dao.list()
        self.__task_view.show_tasks(tasks_to_list)
        