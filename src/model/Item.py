import uuid
import random
from enum import Enum

class Item_State(Enum):
    InStock = 0
    Reserved = 1 
    Processed = 2

class Item(object):
    """
    - id
    - location 
    - destination
    - weight
    - size
    - urgency priority
    """

    def __init__(self):
        self.id = str(uuid.uuid1())  

    def set_parameters(self, weight, size, location, destination, priority):
        self.id = str(uuid.uuid1())  
        self.weight = weight
        self.size = size
        self.location = location
        self.destination = destination
        self.state = Item_State.InStock
        if not priority:
            self.priority = 30
        self.priority = priority
        
    def random_parameters(self, location):
        self.priority = 30
        self.weight = random.randint(1, 100) 
        self.size = random.randint(1, 100) 
        self.location = location

    def update_state(self, state_str):
        if "Reserved" in state_str:
            self.state = Item_State.Reserved
        elif "Processed" in state_str:
            self.state = Item_State.Processed

