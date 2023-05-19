from model.Map import Map   #生成地图
from utils.utils import print2d_with_index   #visualize map, line 13调出map1和map2
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
import concurrent.futures
import pickle
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

#print(35, sys._getframe().f_lineno, f'| 1 = {taskList}', ) # 2023_0509_2323
#print(taskList.get_task_list())

# todo base_on_principle()
"""
for principle_i in principle_list:
    thisWeekItemList = base_on_principle(principle_i, originalItemList)
    for todayItemList in thisWeekItemList:
        ...
"""
taskAssignment_algo_list = ['GA', 'PSO']
for taskAssignment_algo_name in taskAssignment_algo_list:
    c = 0 # firstTime
    total_number_of_session = 5   #定义一共有几次实验，每次session的tasklist都会进行更新迭代 todo
    while c < total_number_of_session:
        # 2023_0509_2223 GA generates this taskList
        taskAssignment_object = TaskAssignment(taskList.get_task_list())
        taskAssignment_object.itemListGeneratedByAlgorithm(taskAssignment_algo_name, notFirstTime=c)
        _list = taskAssignment_object.getItemList()
        session.set_taskList(_list)
        session.process_for_agent(agentManager.agentList)

        # with concurrent.futures.ThreadPoolExecutor(max_workers=NUMBER_OF_AGENT) as executor:
        #     results = executor.map(session.process_for_agent, session.agentManager.agentList) #调用session的process_for_agent函数
        #
        #     for result in results:
        #         print(result)
        #         # statistics todo
        c += 1


# result = session.process_for_agent() #调用session的process_for_agent函数


# one agent in one session
"""
logger.info(agent)
task = Task(agent, _item)
cur_task_accomplish_time = task.compute_a_trip_time()

logger.info(f'This task was accomplished within {cur_task_accomplish_time} s')
logger.info(f'This agent worked {agent.busy_time_so_far} s')
"""


# with open('shelfinfo.pickle','rb') as file:
#    a_dict1=pickle.load(file)
# print(a_dict1)



