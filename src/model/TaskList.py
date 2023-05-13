from utils.Singleton import Singleton

class TaskList(metaclass=Singleton):

    def __init__(self):
        self._list = [] 

    def add_item(self, item):
        self._list.append(item)

    def get_task_list(self):
        return self._list[0:30] # todo to delete chunk
        # return self._list
        
