from model.Shelf import Shelf
from model.ChangerStation import ChangerStation
from utils.logging_stream_handler import logger
from utils import utils

class Map:
    """
    0 - aisle
    1 - shelf
    3 - obstacle
    c - counter
    h - changer home station
    r - rest station
    n - empty
    """
    def __init__(self, scene):  
        self.map = []
        sub = []
        for line in open(scene):   #use file iterators
            for c in line.rstrip():
                sub += c,  #+=加法赋值运算符：sub=sub+c
            self.map.append(sub)
            sub = []

        logger.info('Map is loaded')
        #utils.print2d_with_index(self.map)

    def get_map(self):
        return self.map

    def random_fill_map(self):   #随机生成地图
        for i in range(len(self.map)):   #行的取值范围是默认编辑器的行数
            for j in range(len(self.map[0])):   #定义列的取值范围
                shelf = Shelf((i,j))
                if self.map[i][j] == '1':
                    self.map[i][j] = shelf
                if self.map[i][j] == 'h':
                    self.charger_home_location = (i, j)
                    
    def get_charger_home_location(self):
        return self.charger_home_location

