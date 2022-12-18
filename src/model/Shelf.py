from .Item import Item
from utils import Constants
from .ItemManager import ItemManager

itemManager = ItemManager()
class Shelf:
    """
    item can be picked from both side
    """
    def __init__(self, location):
        self.layer = Constants.SHELF_LAYER
        self.height_ground = 0 
        self.height = Constants.SHELF_HEIGHT 
        """
        self.height_each_layer_list = []
        self.height_each_layer = height/layer  
        for i in range(layer):
            self.height_each_layer_list.append(height_ground)
            self.height_ground += self.height_each_layer
        """
        self.item_on_each_layer = []
        self.location = location
        self.random_fill_shelf()
        self.side_length = Constants.SHELF_SIDE_LENGTH # meter

    def random_fill_shelf(self):
        for i in range(self.layer):
            item = Item()
            item.random_parameters((*self.location, i))
            itemManager.add_item(item)
            self.item_on_each_layer.append(item)

