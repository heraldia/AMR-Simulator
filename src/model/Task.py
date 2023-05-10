from utils import utils
from utils import Constants
from utils.logging_stream_handler import logger
from .Strategy import Strategy
from .AgentManager import AgentManager
from .ItemManager import ItemManager
from .Item import Item_State

agentManager = AgentManager()
itemManager = ItemManager()

class Task:
    """
    self.assignment -> algorithm, methodology
    one task is one trip
    """
    def __init__(self, agent, item, map):
        self.agent = agent
        self.item = item
        # ## 设置地图
        self.map = map
        self.distance = 0
        self.item.update_state("Reserved")
        self.battery_threshold = 0
        #itemManager.remove_item(item)
        #agentManager.update(self.agent, "Idle", "OnDuty")


    def pre_update_battery_threshold(self):
        strategy = Strategy(self.agent, self.item, self.map, 'simple_hamming_distance')

        self.distance = strategy.get_final_path_distance()
        self.battery_threshold = self.distance * self.agent.battery_consumption_rate


    def compute_a_trip_time(self):
        logger.debug(self.agent.location)
        logger.debug(self.item.location)

        # todo
        # self.distance = A_star_algorithm()

        # simple algorithm,
        # strategy = Strategy(self.agent, self.item, self.map, 'simple_hamming_distance')

        # # ## 运行蚁群算法
        # strategy = Strategy(self.agent, self.item, self.map, 'ACO')


        # ## 运行精英蚁群算法
        strategy = Strategy(self.agent, self.item, self.map, 'simple_hamming_distance')

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



    def get_task_info(self):
        res = []
        for item in itemManager.itemList:
            if item.state == Item_State.Processed:
                for agent in agentManager.agentList:
                    if item.id in agent.taskList:
                        res.append(
                            {"机器人ID": agent.id, "物品ID": item.id, "完成时间": agent.cur_task_accomplish_time})
        return res