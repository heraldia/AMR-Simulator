from model.Map import Map
from utils.Singleton import Singleton
import sys
import time
from math import sqrt
from model.ChangerStation import ChangerStation
from utils.logging_stream_handler import logger

class AgentManager(metaclass=Singleton):
    def __init__(self):
        self.agentList = []
        self.agent_state_dict = {
                'Idle'     : [],   #闲置
                'OnDuty'   : [],   #任务中
                'Pausing'  : [],
                'carrying' : [],
                }

    #遍历所有机器人的电量
    def charge(self, agent, map):
        ChargerHome = ChangerStation(map.charger_home_location)
        # 机器人到充电站的距离
        distance_to_charger = sqrt(
            (agent.location[0] - ChargerHome.location[0]) ** 2 + (agent.location[1] - ChargerHome.location[1]) ** 2)

        # 充电速度
        charging_speed = 0.1  # 假设每秒充电0.1度电

        # 计算充电时间
        time_to_charge = (agent.max_battery - agent.current_battery) / charging_speed

        # 机器人在充电时不能执行任务，将其状态设置为pausing
        agent.state = agent.state.Pausing

        # 等待机器人充电完成
        time_elapsed = 0  # 定义时间流逝
        while time_elapsed < time_to_charge:
            time.sleep(1)
            time_elapsed += 1

        # 充电完成，将机器人设置为满点，并将其状态设置为Idle
        agent.current_battery = agent.max_battery
        agent.state = agent.state.Idle

    def check_battery_level(self, checkedAgent):      #检查机器人的电量并决定是否将其发送到充电站,仅仅用来检查单独的机器人的电量，并决定是否将该机器人发送到充电站。
        if checkedAgent.current_battery < checkedAgent.battery_threshold:
            logger.info(f"Agent {checkedAgent.id} is low on battery and needs to charge.")
            # map.charger_home_location.charge(agent)  #发送机器人到充电站充电，调用ChangerStation.py中的charge()方法来充电机器人。

        else:
            logger.info(f"Agent {checkedAgent.id} has sufficient battery level.")


    def check_whole_battery_level(self,charger_home_station):
        for agent in self.agentList:
            if agent.state == "Idle":
                self.check_battery_level(agent.map.charger_home_location)


    def add(self, agent):
        self.agentList.append(agent)
        self.agent_state_dict[agent.state.name].append(agent)

    def update(self, agent, pre_state, cur_state):   #更新agent的状态：删除前一个状态更新当前状态
        #print(18, sys._getframe().f_lineno, f'| 1 = {1}', self.agent_state_dict) # 2022_1217_2349
        self.agent_state_dict[pre_state].remove(agent)
        self.agent_state_dict[cur_state].append(agent)
        agent.update_state(cur_state)

    def analyze_agents(self, result_dict):
        busy_totals = {}
        odometer_totals = {}

        for task in result_dict:
            res = result_dict[task]
            agent = res.task.agent

            if agent.id in ['s0', 's1', 's2', 's3', 's4']:
                if agent.id not in busy_totals:
                    busy_totals[agent.id] = set()
                if agent.id not in odometer_totals:
                    odometer_totals[agent.id] = set()

                if agent.busy_time_so_far not in busy_totals[agent.id]:
                    busy_totals[agent.id].add(agent.busy_time_so_far)

                if agent.odometer not in odometer_totals[agent.id]:
                    odometer_totals[agent.id].add(agent.odometer)

        for agent in self.agentList:
            busy_total = sum(busy_totals.get(agent.id, []))
            odometer_total = sum(odometer_totals.get(agent.id, []))
            logger.info(
                f"agent{agent.id}, Total busy time: {busy_total} second; Total odometer: {odometer_total} meter.")


    def has_pending_items(self):
        return bool(self.agent_state_dict['OnDuty']) or bool(self.agent_state_dict['Pausing']) or bool(
            self.agent_state_dict['carrying'])