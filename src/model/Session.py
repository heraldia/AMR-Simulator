import multiprocessing
from .AgentManager import AgentManager
from .ItemManager import ItemManager
from .Task import Task
from utils.logging_stream_handler import logger
import sys
import pickle
from .Shelf import Shelf


class Session:
    """
    In a certain map with loaded shelves, a session is {that some agents complish a item_list (from self.itemManager)}
    """


    def __init__(self, map, agentManager, itemManager):
        self.cur_task_accomplish_time = None
        only_fetch_item = True
        # fetch_and_replenish_item
        self.totalHours = 0
        self.map = map
        self.agentManager = agentManager
        self.itemManager = itemManager
        self.item_list = []  # 添加item_list属性
        self.cur_task_accomplish_time = 0  # 添加 cur_task_accomplish_time 属性

    #设置地图
    def set_map(self, map):
        self.map = map

    # sequential, one trip for one item.
    def process_for_agent(self, _agent):
        task_dict={}
        i=0



        while self.itemManager.get_number_of_items():
            _item = self.itemManager.pick_an_item_from_head()
            if self.agentManager.agent_state_dict["Idle"]:
                _agent = self.agentManager.agent_state_dict["Idle"][0]
                self.agentManager.update(_agent, "Idle", "OnDuty")
                task = Task(_agent, _item, self.map)
                task_dict[i]=[tuple(_agent.location), tuple(_item.location), _agent.id, _item.id, self.cur_task_accomplish_time]  # 将 cur_task_accomplish_time 添加到 item_dict
                i=i+1
                task.pre_update_battery_threshold() #更新当前task中的battery_threshold
                self.agentManager.check_battery_level(task.agent, task.battery_threshold, self.map)
                self.cur_task_accomplish_time = task.compute_a_trip_time()
                logger.info(f"{_agent.id}, {_item.id}")
                logger.info(f'This task was accomplished within {self.cur_task_accomplish_time} s')
                logger.info(f'This agent worked {_agent.busy_time_so_far} s')

        self.agentManager.analyze_agents()




        file = open('shelfinfo.pickle', 'wb')
        pickle.dump(task_dict, file)
        file.close()
