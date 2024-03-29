from utils.Singleton import Singleton

class TaskList(metaclass=Singleton):

    def __init__(self):
        self._list = [] 

    def add_item(self, item):
        self._list.append(item)


    def get_task_list(self):
        self._list.sort(key=lambda item: item.priority, reverse=True) # sort by priority for the tasklist
        return self._list # todo to delete chunk
        # return self._list
        
