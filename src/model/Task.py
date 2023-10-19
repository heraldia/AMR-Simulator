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
    def __init__(self, agent, item_list, map):
        self.agent = agent
        self.item_list = item_list
        # ## 设置地图
        self.map = map
        self.distance = 0
        for item in self.item_list:
            item.update_state("Reserved")
        self.battery_threshold = 0
        #itemManager.remove_item(item)
        #agentManager.update(self.agent, "Idle", "OnDuty")

    def pre_update_battery_threshold(self):
        total_distance = 0
        for item in self.item_list:
            strategy = Strategy(self.agent, item, self.map, 'a_star')
            item_distance = strategy.get_final_path_distance()
            total_distance += item_distance
            self.agent.location = item.location[:2]
        self.distance = total_distance
        self.battery_threshold = self.distance * self.agent.battery_consumption_rate
        self.agent.location = self.map.charger_home_location


    def compute_a_trip_time(self):
        total_distance = 0
        total_time = 0
        for item in self.item_list:
            logger.debug(self.agent.location)
            logger.debug(item.location)



            # todo
            # self.distance = A_star_algorithm()

            # simple algorithm,
            # strategy = Strategy(self.agent, self.item, self.map, 'simple_hamming_distance')

            # # ## 运行蚁群算法
            # strategy = Strategy(self.agent, self.item, self.map, 'ACO')


            # ## 运行精英蚁群算法
            strategy = Strategy(self.agent, item, self.map, 'a_star')
            item_distance = strategy.get_final_path_distance()
            total_distance += item_distance
            item_height = item.location[2] * Constants.SHELF_HEIGHT / Constants.SHELF_LAYER
            item_time = item_distance * Constants.SHELF_SIDE_LENGTH / self.agent.moving_speed + item_height / self.agent.rising_arm_speed + item_height / self.agent.dropping_arm_speed + 2 * self.agent.turning_time + self.agent.fetching_time + self.agent.dispatching_time
            total_time += item_time
            self.agent.location = item.location[:2]

        self.distance = total_distance
        self.task_fulfill_time = total_time
        self.agent.update_odometer(self.distance)
        self.agent.update_busy_time_accumulated(self.task_fulfill_time)
        self.processed_item()
        self.agent.location = self.map.charger_home_location
    
        return self.task_fulfill_time    

    def processed_item(self):
        for item in self.item_list:
            item.update_state("Processed")
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