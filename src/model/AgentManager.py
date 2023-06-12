from model.ChangerStation import ChangerStation
from utils.logging_stream_handler import logger

from utils.Singleton import Singleton
from model.Map import Map
from math import sqrt
import pandas as pd
import os
import sys
import time





class AgentManager(metaclass=Singleton):
    def __init__(self):
        self.agentList = []
        self.fitness_results = []
        self.agent_state_dict = {
                'Idle'     : [],   #闲置
                'OnDuty'   : [],   #任务中
                'Pausing'  : [],
                'carrying' : [],
                }
        self.experiment_counter = 0 # 实验计数器
        self.df = pd.DataFrame(columns=['Experiment', 'Agent', 'Busy Time', 'Odometer', "Fitness Number"]) # 创建一个空的DataFrame


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
        # agent.location = map.charger_home_location

        # 等待机器人充电完成
        time_elapsed = 0  # 定义时间流逝
        while time_elapsed < time_to_charge:
            # time.sleep(1)
            time_elapsed += 1

        # 充电完成，将机器人设置为满点，并将其状态设置为Idle
        agent.current_battery = agent.max_battery
        agent.state = agent.state.Idle

    def check_battery_level(self, checkedAgent, battery_threshold, map):      #检查机器人的电量并决定是否将其发送到充电站,仅仅用来检查单独的机器人的电量，并决定是否将该机器人发送到充电站。
        if checkedAgent.current_battery < battery_threshold:
            logger.info(f"Agent {checkedAgent.id} is low on battery and needs to charge.")
            self.charge(checkedAgent, map)  # 调用charge()方法来充电机器人。
            logger.info(f"Agent {checkedAgent.id} has been fully charged.")
            # map.charger_home_location.charge(agent)  #发送机器人到充电站充电，调用ChangerStation.py中的charge()方法来充电机器人。

        else:
            logger.info(f"Agent {checkedAgent.id} has sufficient battery level.")


    #def check_whole_battery_level(self,charger_home_station):
     #   for agent in self.agentList:
      #      if agent.state == "Idle":
       #         self.check_battery_level(agent.map.charger_home_location)


    def add(self, agent):
        self.agentList.append(agent)
        self.agent_state_dict[agent.state.name].append(agent)

    def update(self, agent, pre_state, cur_state):   #更新agent的状态：删除前一个状态更新当前状态
        #print(18, sys._getframe().f_lineno, f'| 1 = {1}', self.agent_state_dict) # 2022_1217_2349
        self.agent_state_dict[pre_state].remove(agent)
        self.agent_state_dict[cur_state].append(agent)
        agent.update_state(cur_state)


    def analyze_agents(self, task_list, record_fitness=True, record_data = True):
        global agent
        self.experiment_counter += 1 #Increase the experiment counter at the beginning of each experiment
        total_busy_time = 0
        total_odometer = 0
        for i, agent in enumerate(self.agentList):
            logger.info(f"agent{i}, busy = {agent.busy_time_so_far} second; odometer = {agent.odometer} meter.")
            total_busy_time += agent.busy_time_so_far
            total_odometer += agent.odometer
            temp_df = pd.DataFrame(
                [{'Experiment': self.experiment_counter, 'Agent': f"agent{i}", 'Busy Time': agent.busy_time_so_far,
                  'Odometer': agent.odometer}], columns=['Experiment', 'Agent', 'Busy Time', 'Odometer'])
            self.df = pd.concat([self.df, temp_df], ignore_index=True)

        fitness_number = total_busy_time + total_odometer


        if record_fitness:
            self.fitness_results.append(fitness_number)
        logger.info("fitness number is {}".format(self.fitness_results))
        temp_df = pd.DataFrame([{'Experiment': self.experiment_counter, 'Agent': 'Total', 'Busy Time': total_busy_time,
                                 'Odometer': total_odometer, 'Fitness Number': fitness_number}],
                               columns=['Experiment', 'Agent', 'Busy Time', 'Odometer', 'Fitness Number'])
        self.df = pd.concat([self.df, temp_df], ignore_index=True)
        # Save to Excel after each experiment

        return fitness_number

    def write_to_excel(self):
            self.df.to_excel("Agents_Statistics.xlsx", index=False)
