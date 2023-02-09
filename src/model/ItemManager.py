from utils.Singleton import Singleton

class ItemManager(metaclass=Singleton):
    def __init__(self):
        self.itemList = []

    def add_item(self, item):
        self.itemList.append(item)

    def pick_an_item(self):
        item = self.itemList.pop()  #用于移除列表中的一个元素(默认最后一个元素)，并且返回该元素的值2
        return item

    def remove_item(self, item):
        try:
            self.itemList.remove(item)
        except Exception as e:
            print (e)
            raise e

    def get_number_of_items(self):
        return len(self.itemList)
