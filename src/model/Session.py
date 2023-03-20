from .Task import Task
from utils.logging_stream_handler import logger
import pickle
import multiprocessing
from .result import result
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


    # 设置地图
    def set_map(self, map):
        self.map = map

    # sequential, one trip for one item.
    def process(self):

        item_dict = {}
        j = 0


        # Robot quantity
        n_agents = len(self.agentManager.agentList)

        # 创建进程池
        pool = multiprocessing.Pool(processes=n_agents)

        # 创建空的任务列表
        tasks = []


        #保存所有的result对象到字典中：
        result_dict = {}


        while self.itemManager.get_number_of_items():
            _item = self.itemManager.pick_an_item()
            # ## 如果item是Shelf
            if type(self.map.get_map()[_item.location[0]][_item.location[1]]) == Shelf:
                if self.agentManager.agent_state_dict["Idle"]:
                    _agent = self.agentManager.agent_state_dict["Idle"][0]
                    task = Task(_agent, _item, self.map, self.agentManager, self.itemManager)
                    item_dict[j] = [tuple(_agent.location), tuple(_item.location), _agent.id, _item.id, self.cur_task_accomplish_time]  # 将 cur_task_accomplish_time 添加到 item_dict
                    j = j + 1

                    self.agentManager.update(task.agent, "Idle", "OnDuty")


                    result_dict[task] = None      #将result对象保存到字典中
                    tasks.append(task)

                else:
                    for k in range(len(self.agentManager.agent_state_dict["OnDuty"])):
                        currentAgent = self.agentManager.agent_state_dict["OnDuty"][0]

                        self.agentManager.update(currentAgent, "OnDuty", "Idle")





        file = open('shelfinfo.pickle', 'wb')
        pickle.dump(item_dict, file)
        file.close()



        results = pool.map(self.run_agent_task, tasks)  # 更新保存的result对象
        for i, res in enumerate(results):
            result_dict[tasks[i]] = res

        self.agentManager.analyze_agents(result_dict)  # results里面，每一个task下的agent的值是已经运行过后的值，而agentManager.agentList里面只有当前运行的agent的值是变化的，其他是没有变化的。

        pool.close()
        pool.join()


    def run_agent_task(self, task):
        # self.agentManager.check_battery_level(task.agent)
        # self.agentManager.charge(task.agent, self.map)
        self.cur_task_accomplish_time = task.compute_a_trip_time()

        logger.info(f"{task.agent.id}, {task.item.id}")
        logger.info(f'This task was accomplished within {self.cur_task_accomplish_time} s')
        logger.info(f'This agent worked {task.agent.busy_time_so_far} s')

        res = result(task)

        return res

