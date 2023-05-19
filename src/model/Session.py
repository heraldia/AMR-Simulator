from .AgentManager import AgentManager
from .ItemManager import ItemManager
from .Task import Task
from utils.logging_stream_handler import logger
import sys
import pickle
import copy
from .Shelf import Shelf


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


    #设置地图
    def set_map(self, map):
        self.map = map

    def set_taskList(self, taskList):
        self.taskList = taskList

    # sequential, one trip for one item.
    def process_for_agent(self, _agent):
        task_dict={}
        i=0
        item_list=[]
        processed_items = []
        queue = copy.deepcopy(self.taskList)
        agentList = self.agentManager.agentList
        for agent in agentList:
            agent.state = "Idle"
            agent.odometer = 0
            agent.busy_time_so_far = 0
            agent.battery_level = 100

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


                sub_process_for_agent(_agent, item_list)
                self.agentManager.analyze_agents()
                item_list = []






        # # print(42, sys._getframe().f_lineno, f'| 1 = {self.taskList}', ) # 2023_0512_2111
        #
        # for _item in self.taskList:
        #     if self.agentManager.agent_state_dict["Idle"]:
        #         _agent = self.agentManager.agent_state_dict["Idle"][0]
        #         self.agentManager.update(_agent, "Idle", "OnDuty")
        #         for _item in self.taskList:
        #             if _item not in processed_items and _agent.add_item_to_agent(_item):
        #                 item_list.append(_item)
        #                 processed_items.append(_item)
        #                 # self.taskList.remove(_item)
        #             else:
        #                 break
        #         self.taskList = [item for item in self.taskList if item not in processed_items]
        #         if not self.taskList or item_list:  # if taskList is empty or item_list is not empty
        #             task = Task(_agent, item_list, self.map)
        #             task_dict[i] = [tuple(_agent.location), tuple(_item.location), _agent.id, _item.id,
        #                             self.cur_task_accomplish_time]  # 将 cur_task_accomplish_time 添加到 item_dict
        #             i = i + 1
        #             task.pre_update_battery_threshold()  # 更新当前task中的battery_threshold
        #             self.agentManager.check_battery_level(task.agent, task.battery_threshold, self.map)
        #             self.cur_task_accomplish_time = task.compute_a_trip_time()
        #             logger.info(f"{_agent.id}, {_item.id}")
        #             logger.info(f'This task was accomplished within {self.cur_task_accomplish_time} s')
        #             logger.info(f'This agent worked {_agent.busy_time_so_far} s')
        #             item_list = []







        file = open('shelfinfo.pickle', 'wb')
        pickle.dump(task_dict, file)
        file.close()
