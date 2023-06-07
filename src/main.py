from model.Map import Map   #生成地图
from utils.utils import print2d_with_index   #visualize map
from utils.logging_stream_handler import logger    #logger函数监控整个项目
from model.Agent import Agent   #定义搬运机器人
from model.AgentManager import AgentManager   #定义机器人管理单位
from model.ItemManager import ItemManager
from model.TaskAssignment import TaskAssignment
from model.Task import Task   #定义任务和需求
from model.TaskList import TaskList   #
from model.ChangerStation import ChangerStation     #定义充电点
from model.Session import Session    #定义一次从头到尾的实验
from utils.Constants import NUMBER_OF_AGENT    #定义一些永远不变的函数
from model.GA import GA
import threading
import sys


map = Map("data/scene.dat")

logger.debug (map.get_map()[1][2])

map.random_fill_map()
# print2d_with_index(map.get_map())

shelf = map.get_map()[1][2]
_item = shelf.item_on_each_layer[0]   #定义item放在架子的每一层上，从第一个元素开始
logger.info(_item.weight)   #监控item的weight, size和location，可以自己定义
logger.info(_item.size)
logger.info(_item.location)

charger_home_location = map.get_charger_home_location()
logger.info(charger_home_location)   #监控charger home location

charger_station = ChangerStation(charger_home_location)

agentManager = AgentManager()
for i in range(NUMBER_OF_AGENT):
    agent = Agent('s', i)
    agent.set_location(charger_home_location)
    agentManager.add(agent)

itemManager = ItemManager()
taskList = TaskList()
session = Session(map, agentManager)
# ## 设置地图进去
session.set_map(map)

# todo base_on_principle()
"""
for principle_i in principle_list:
    thisWeekItemList = base_on_principle(principle_i, originalItemList)
    for todayItemList in thisWeekItemList:
        ...
"""
ga_object = None
# taskAssignment_algo_list = ['GA', 'PSO']
taskAssignment_algo_list = ['GA']
for taskAssignment_algo_name in taskAssignment_algo_list:
    c = 0 #initial generation
    total_number_of_session = 10   #定义一共100次GA的迭代，每次session的tasklist都会进行更新迭代
    while c < total_number_of_session:
        # 2023_0509_2223 GA generates this taskList
        taskAssignment_object = TaskAssignment(taskList.get_task_list(), ga_object=ga_object)
        total_itemList = taskAssignment_object.itemListGeneratedByAlgorithm(taskAssignment_algo_name, notFirstTime=c)


        if c == 0 or not total_itemList:
            ga_object = taskAssignment_object.ga_object
            _list = taskAssignment_object.getItemList()
            session.set_taskList(_list)
            # session.process_for_agent(agentManager.agentList)
            for agent in session.agentManager.agentList:
                agent.state = "Idle"
                agent.odometer = 0
                agent.busy_time_so_far = 0
                agent.current_battery = 100

            threads = []
            for i in range(NUMBER_OF_AGENT):
                t = threading.Thread(target=session.process_for_agent)
                threads.append(t)
                t.start()

            for thread in threads:
                thread.join()

            agentManager.analyze_agents(record_fitness=False if c == 0 else True)
            agentManager.write_to_excel()  # Write to excel after each experiment


            #     for result in results:
            #         print(result)
            #         # statistics todo

            c += 1


        else:

            agentManager.fitness_results = []
            for _list in total_itemList:
                taskAssignment_object_new= TaskAssignment(_list)
                new_list = taskAssignment_object_new.getItemList()
                session.set_taskList(new_list)

                for agent in session.agentManager.agentList:
                    agent.state = "Idle"
                    agent.odometer = 0
                    agent.busy_time_so_far = 0
                    agent.current_battery =0

                threads = []
                for i in range(NUMBER_OF_AGENT):
                    t = threading.Thread(target=session.process_for_agent)
                    threads.append(t)
                    t.start()

                for thread in threads:
                    thread.join()

                agentManager.analyze_agents()
                agentManager.write_to_excel()  # Write to excel after each experiment
                # statistics for tasklist in each experiment. todo
            c += 1


# one agent in one session
"""
logger.info(agent)
task = Task(agent, _item)
cur_task_accomplish_time = task.compute_a_trip_time()

logger.info(f'This task was accomplished within {cur_task_accomplish_time} s')
logger.info(f'This agent worked {agent.busy_time_so_far} s')
"""



