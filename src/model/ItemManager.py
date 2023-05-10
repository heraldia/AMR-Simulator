from utils.Singleton import Singleton
from .Item import Item
import random
import sys

class ItemManager(metaclass=Singleton):
    def __init__(self, len_item_list=None, initItemList = None):
        print(7, sys._getframe().f_lineno, f'| 1 = {initItemList}', ) # 2023_0509_2340
        if not initItemList:
            self.itemList = []
        else:
            self.itemList = initItemList[:]
        self.len_item_list = 100

    def add_item(self, item):
        self.itemList.append(item)

    def pick_an_item_from_end(self):
        item = self.itemList.pop()  #用于移除列表中的一个元素(默认最后一个元素)，并且返回该元素的值2
        return item

    def pick_an_item_from_head(self):
        #self.itemList = reversed(self.itemList)
        self.itemList.reverse()

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

    def get_a_random_item_list(self, map):
        _list = []
        i = self.len_item_list
        while i:
            item = Item()
            x = random.randint(0, len(map))
            y = random.randint(0, len(map[0]))
            z = random.randint(0,3)
            item.random_parameters((x,y,z))
            _list.append(item)
            self.itemList.append(item)
            i -= 1
        return _list
