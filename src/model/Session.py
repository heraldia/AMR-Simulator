from .AgentManager import AgentManager
from .ItemManager import ItemManager
from .Task import Task
from utils.logging_stream_handler import logger
import sys
import pickle

agentManager = AgentManager()
itemManager = ItemManager()

class Session:

    def __init__(self):
        only_fetch_item = True
        # fetch_and_replenish_item
        self.totalHours = 0

    # sequential, one trip for one item.
    def process(self):
        item_dict={}
        i=0
        while itemManager.get_number_of_items():
            _item = itemManager.pick_an_item()
            if agentManager.agent_state_dict["Idle"]:
                _agent = agentManager.agent_state_dict["Idle"][0]
                agentManager.update(_agent, "Idle", "OnDuty")
                task = Task(_agent, _item)
                item_dict[i]=task.item.location
                i=i+1
                cur_task_accomplish_time = task.compute_a_trip_time()
                logger.info(f"{_agent.id}, {_item.id}")
                logger.info(f'This task was accomplished within {cur_task_accomplish_time} s')
                logger.info(f'This agent worked {_agent.busy_time_so_far} s')

            agentManager.analyze_agents()


        file = open('shelfinfo.pickle', 'wb')
        pickle.dump(item_dict, file)
        file.close()
    
