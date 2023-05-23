from utils.logging_stream_handler import logger
from .AgentManager import AgentManager
from .ItemManager import ItemManager
from .Shelf import Shelf
from .Task import Task
import sys
import copy
import threading



class Session:
    """
    In a certain map with loaded shelves, a session is {that some agents accomplish a taskList (from self.itemManager)}
    """


    def __init__(self, map, agentManager):
        self.cur_task_accomplish_time = None
        only_fetch_item = True
        # fetch_and_replenish_item
        self.totalHours = 0
        self.map = map
        self.agentManager = agentManager
        #self.itemManager = itemManager
        self.taskList = []
        self.cur_task_accomplish_time = 0  # 添加 cur_task_accomplish_time 属性
        self.all_item_list = []



    #设置地图
    def set_map(self, map):
        self.map = map

    def set_taskList(self, taskList):
        self.taskList = taskList
        self.processingTaskList = copy.deepcopy(taskList)

    # sequential, one trip for one item.
    def process_for_agent(self):
        item_list=[]
        processed_items = []
        queue = self.processingTaskList


        while queue:
            while self.agentManager.agent_state_dict["Idle"]:
                _agent = self.agentManager.agent_state_dict["Idle"][0]
                if not queue:
                    return
                for _item in queue:
                    if _agent.add_item_to_agent(_item):
                        _item = queue.pop(0)
                        item_list.append(_item)
                        processed_items.append(_item)

                    else:
                        break

                def sub_process_for_agent(_agent, item_list):
                    self.agentManager.update(_agent, "Idle", "OnDuty")
                    task = Task(_agent, item_list, self.map)
                    task.pre_update_battery_threshold()  # 更新当前task中的battery_threshold
                    self.agentManager.check_battery_level(task.agent, task.battery_threshold, self.map)
                    self.cur_task_accomplish_time = task.compute_a_trip_time()
                    logger.info(f"{_agent.id}, {_item.id}")
                    logger.info(f'This task was accomplished within {self.cur_task_accomplish_time} s')
                    logger.info(f'This agent worked {_agent.busy_time_so_far} s')
                    self.all_item_list.append(item_list)


                sub_process_for_agent(_agent, item_list)
                item_list = []
                self.agentManager.analyze_agents()




