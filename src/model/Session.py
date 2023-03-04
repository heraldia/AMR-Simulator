from .AgentManager import AgentManager
from .ItemManager import ItemManager
from .Task import Task
from utils.logging_stream_handler import logger
import sys
import pickle
from .Shelf import Shelf


class Session:


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
    def process(self):
        item_dict={}
        i=0


        while self.itemManager.get_number_of_items():
            _item = self.itemManager.pick_an_item()
            # ## 如果item是Shelf
            if type(self.map.get_map()[_item.location[0]][_item.location[1]]) == Shelf:
                if self.agentManager.agent_state_dict["Idle"]:
                    _agent = self.agentManager.agent_state_dict["Idle"][0]
                    self.agentManager.update(_agent, "Idle", "OnDuty")
                    task = Task(_agent, _item, self.map)
                    item_dict[i]=[tuple(_agent.location), tuple(_item.location), _agent.id, _item.id, self.cur_task_accomplish_time]  # 将 cur_task_accomplish_time 添加到 item_dict
                    i=i+1
                    self.agentManager.charge(task.agent,self.map)
                    self.agentManager.check_battery_level(task.agent)
                    self.cur_task_accomplish_time = task.compute_a_trip_time()
                    logger.info(f"{_agent.id}, {_item.id}")
                    logger.info(f'This task was accomplished within {self.cur_task_accomplish_time} s')
                    logger.info(f'This agent worked {_agent.busy_time_so_far} s')

                self.agentManager.analyze_agents()


        file = open('shelfinfo.pickle', 'wb')
        pickle.dump(item_dict, file)
        file.close()
    
