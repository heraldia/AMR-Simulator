from enum import Enum


class State(Enum):
    """
    state = static, running.
    ## state, FSM finite state machine.
    - idle / init
    - run after accept
    - pausing, cross section.
    - idle / accomplished
    """
    Idle = 0  #闲置
    OnDuty = 1   #任务中
    Pausing = 2   #暂停
    

class Agent:
    """
    parameters, specifications,
    talk to center control

    mins_to_charged_full
    mins_alive
    mins_working
    mins_time_to_die

    acceloration_rate
    deceloration_rate
    goForward
    turnClockwise
    turnCounterClockwise
    multithread
    """

    def __init__(self, _type, seq_num):
        self.type = _type
        self.id = _type + str(seq_num)
        self.state = State.Idle
        self.odometer = 0
        self.weight_this_trip = 0
        self.idle_time_so_far = 0
        self.busy_time_so_far = 0
        self.init_location()
        self.current_battery = 100  #初始电量为100
        self.max_battery = 100  #最大电量为100
        self.max_load = 200
        self.battery_threshold = 20  #假设电量低于20度电时需要充电
        self.moving_speed = 0.5 # m/s
        self.rising_arm_speed = 0.1 # m/s
        self.dropping_arm_speed = 0.1 # m/s
        self.turning_time = 1 # s
        #完成一个任务需要：移动，举起机械臂，放下机械臂，转弯，取货，放货

        self.fetching_time = 1 # s
        self.dispatching_time = 1 # s
        self.battery_consumption_rate = 0.1  ## 电量消耗率，表示每走1m机器人消耗10%电量



    def init_location(self, location = None):
        if not location:
            location = (0,0)
        self.location = location


    def set_location(self, location):
        self.location = location


    def increment_odometer(self):    #定义距离的增加（自增1）
        self.odometer += 1   #原始值增加1
        # self.consume_battery(1)

    def update_odometer(self, travelled_distance):#自定义距离的增加，传进来多少增加多少
        self.odometer += travelled_distance   #odometer=odometer+travelled_distance\
        consumption = travelled_distance * self.battery_consumption_rate  # 计算消耗的电量
        self.current_battery -= consumption  # 更新机器人的电量

    def idle_time_accumulated(self):
        self.idle_time_so_far += 1

    def update_busy_time_accumulated(self, time_duration):
        self.busy_time_so_far += time_duration 

    def reset_weight(self):
        self.weight_this_trip = 0

    def increase_weight(self, item_weight):
        self.weight_this_trip += item_weight

    def add_item_to_agent(self,item):
        if self.weight_this_trip + item.weight > self.max_load:
            #back to home(charger station)
            # self.update_state("Idle")
            self.reset_weight()
            return False
        else:
            self.increase_weight(item.weight)
            # next trip
            return True


    def update_state(self, state_str):
        if "Idle" in state_str:
            self.state = State.Idle
        elif "OnDuty" in state_str:
            self.state = State.OnDuty
        elif "Pausing" in state_str:
            self.state = State.Pausing





