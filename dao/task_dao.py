import json
from datetime import datetime
from model.task import Task

class TaskDAO:
    def __init__(self, file="task.json"):
        self.__file_path = file
        self.__tasks = self.__load()
        
    def __load(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                tasks = []
                
                for d in data:
                    creation_date = datetime.strptime(d['creation_date'], '%Y-%m-%d %H:%M')
                    if d.get('completion_date'):
                        completion_date = datetime.strptime(d['completion_date'], '%Y-%m-%d %H:%M')
                    else:
                        completion_date = None
                    
                    task = Task(
                        description=d['description'],
                        status=d['status'],
                        creation_date=creation_date,
                        completion_date=completion_date
                    )
                    
                    tasks.append(task)
                return tasks
        except FileNotFoundError:
            return []
    
    def __save(self):
        task_info = []
        for task in self.__tasks:
            data = task.get_data()
            data["creation_date"] = task.created.strftime('%Y-%m-%d %H:%M')
            if data["completion_date"] != None:
                data["completion_date"] = task.completed.strftime('%Y-%m-%d %H:%M')
        
            task_info.append(data)
        
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(task_info, file, indent=4, ensure_ascii=False)
            
    def add(self, task: Task):
        self.__tasks.append(task)
        self.__save()
        
    def remove(self, task: Task):
        self.__tasks.remove(task)
        self.__save()
        
    def update(self):
        self.__save()
    
    def list(self):
        return self.__tasks
        