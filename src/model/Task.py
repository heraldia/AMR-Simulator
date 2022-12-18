from utils import utils
from utils import Constants
from utils.logging_stream_handler import logger
from .Strategy import Strategy
from .AgentManager import AgentManager
from .ItemManager import ItemManager

agentManager = AgentManager()
itemManager = ItemManager()

class Task:
    """
    self.assignment -> algorithm, methodology
    one task is one trip
    """
    def __init__(self, agent, item):
        self.agent = agent
        self.item = item
        self.item.update_state("Reserved")
        #itemManager.remove_item(item)
        #agentManager.update(self.agent, "Idle", "OnDuty")


    def compute_a_trip_time(self):
        logger.debug(self.agent.location)
        logger.debug(self.item.location)

        # todo
        # self.distance = A_star_algorithm()

        # simple algorithm, 
        strategy = Strategy(self.agent, self.item, 'simple_hamming_distance')
        self.distance = strategy.get_final_path_distance()

        item_height = self.item.location[2] * Constants.SHELF_HEIGHT / Constants.SHELF_LAYER 
        self.task_fulfill_time = self.distance * Constants.SHELF_SIDE_LENGTH / self.agent.moving_speed + item_height / self.agent.rising_arm_speed + item_height / self.agent.dropping_arm_speed + 2 * self.agent.turning_time + self.agent.fetching_time + self.agent.dispatching_time

        self.agent.update_odometer(self.distance)
        self.agent.update_busy_time_accumulated(self.task_fulfill_time)
        self.processed_item()
    
        return self.task_fulfill_time    

    def processed_item(self):
        self.item.update_state("Processed")
        self.agent.update_state("Idle")
        agentManager.update(self.agent, "OnDuty", "Idle")



