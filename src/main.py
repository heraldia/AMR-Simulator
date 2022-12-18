from model.Map import Map
from utils.utils import print2d_with_index
from utils.logging_stream_handler import logger
from model.Agent import Agent
from model.AgentManager import AgentManager
from model.Task import Task
from model.ChangerStation import ChangerStation
from model.Session import Session
from utils.Constants import NUMBER_OF_AGENT


map = Map("data/scene.dat")
logger.debug (map.get_map()[1][2])

map.random_fill_map()
#print2d_with_index(map.get_map())

shelf = map.get_map()[1][2]
_item = shelf.item_on_each_layer[0]
logger.info(_item.weight)
logger.info(_item.size)
logger.info(_item.location)

charger_home_location = map.get_charger_home_location()
logger.info(charger_home_location)
charger_station = ChangerStation(charger_home_location)

agentManager = AgentManager()
for i in range(NUMBER_OF_AGENT):
    agent = Agent('s', i)
    agent.set_location(charger_home_location)
    agentManager.add(agent)

# one agent in one session
"""
logger.info(agent)
task = Task(agent, _item)
cur_task_accomplish_time = task.compute_a_trip_time()

logger.info(f'This task was accomplished within {cur_task_accomplish_time} s')
logger.info(f'This agent worked {agent.busy_time_so_far} s')
"""

session = Session()
session.process()




