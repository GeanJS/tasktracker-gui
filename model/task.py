from datetime import datetime

class Task:
    def __init__(self, description: str, status: str, creation_date: datetime, completion_date = None):
        self.__description = description
        self.__status = status
        self.__created = creation_date
        self.__completed = completion_date
        
        
    @property
    def description(self) -> str:
        return self.__description
    
    @description.setter
    def description(self, new_description: str):
        self.__description = new_description
        
    @property
    def status(self) -> str:
        return self.__status
    
    @status.setter
    def status(self, new_status: str):
        self.__status = new_status
        
    @property
    def created(self) -> datetime:
        return self.__created
    
    @property
    def completed(self):
        return self.__completed
    
    @completed.setter
    def completed(self, new_date: datetime):
        self.__completed = new_date
        
        
    def get_data(self):
        return {
            "descriptiom": self.__description,
            "status": self.__status,
            "creation_date": self.__created,
            "completion_date": self.__completed
        }