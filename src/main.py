import multiprocessing
import sys

if __name__ == '__main__':
    multiprocessing.freeze_support()
    if sys.platform == 'win32':
        multiprocessing.set_start_method('spawn')

    from model.Map import Map   #生成地图
    from utils.utils import print2d_with_index   #visualize map, line 13调出map1和map2
    from utils.logging_stream_handler import logger    #logger函数监控整个项目
    from model.Agent import Agent   #定义搬运机器人
    from model.AgentManager import AgentManager   #定义机器人管理单位
    from model.ItemManager import ItemManager
    from model.Task import Task   #定义任务和需求
    from model.ChangerStation import ChangerStation     #定义充电点
    from model.Session import Session    #定义一次从头到尾的实验
    from utils.Constants import NUMBER_OF_AGENT    #定义一些永远不变的函数
    import pickle




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


    itemManager = ItemManager()


    agentManager = AgentManager()
    for i in range(NUMBER_OF_AGENT):
        agent = Agent('s', i)
        agent.set_location(charger_home_location)
        agentManager.add(agent)


    # session = Session()
    session = Session(map, agentManager, itemManager)
    # ## 设置地图进去
    session.set_map(map)
    result = session.process()



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




