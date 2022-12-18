from utils.Singleton import Singleton
import sys
from utils.logging_stream_handler import logger

class AgentManager(metaclass=Singleton):
    def __init__(self):
        self.agentList = []
        self.agent_state_dict = {
                'Idle'     : [],
                'OnDuty'   : [],
                'Pausing'  : [],
                'carrying' : [],
                }

    def add(self, agent):
        self.agentList.append(agent)
        self.agent_state_dict[agent.state.name].append(agent)

    def update(self, agent, pre_state, cur_state):
        #print(18, sys._getframe().f_lineno, f'| 1 = {1}', self.agent_state_dict) # 2022_1217_2349
        self.agent_state_dict[pre_state].remove(agent)
        self.agent_state_dict[cur_state].append(agent)

    def analyze_agents(self):
        for i, agent in enumerate(self.agentList):
            logger.info(f"agent{i}, busy = {agent.busy_time_so_far} second; odometer = {agent.odometer} meter.")


