import numpy as np
import copy

class Ant():
    def __init__(self,max_step,pher_imp,dis_imp) -> None:
        self.max_step = max_step    # 蚂蚁最大行动力
        self.pher_imp = pher_imp    # 信息素重要性系数
        self.dis_imp = dis_imp      # 距离重要性系数
        self.destination = [19,19]  # 默认的终点节点(在run方法中会重新定义该值)
        self.successful = True      #标志蚂蚁是否成功抵达终点
        

    def run(self,map_data,pher_data,posi = None,dest = None):
        self.record_way = [posi]   #路径节点信息记录
        #Step 0:把蚂蚁放在起点处
        if posi == None:
            self.position = [0,0]       #蚂蚁初始位置[y,x] = [0,0],考虑到列表索引的特殊性，先定y，后定x
        else:
            self.position = posi
        if dest == None:
            self.destination = [len(map_data)-1, len(map_data)-1]
        else:
            self.destination = dest
        #Step 1:不断找下一节点，直到走到终点或者力竭 
        for i in range(self.max_step):
            r = self.select_next_node(map_data,pher_data)
            if r == False:
                self.successful = False
                break
            else:
                if self.position == self.destination:
                    break
        else:
            self.successful = False
    
    def select_next_node(self,map_data,pher_data):
        '''
        Function:
        ---------
        选择下一节点，结果直接存入self.postion，仅返回一个状态码True/False标志选择的成功与否。
        '''
        y_1 = self.position[0]
        x_1 = self.position[1]
        #Step 1:计算理论上的周围节点
        node_be_selected = [[y_1-1,x_1-1],[y_1-1,x_1],[y_1-1,x_1+1],     #上一层
                            [y_1,x_1-1],              [y_1,x_1+1],       #同层
                            [y_1+1,x_1-1],[y_1+1,x_1],[y_1+1,x_1+1],     #下一层
                        ]
        node_be_selected_2 = [[y_1-1,x_1],     #上一层
                            [y_1,x_1-1],              [y_1,x_1+1],       #同层
                            [y_1+1,x_1]     #下一层
                        ]
        if self.destination in node_be_selected_2:   # 如果到达终点旁，则直接选中终点
            self.position = self.destination
            self.record_way.append(copy.deepcopy(self.position))
            map_data[self.position[0]][self.position[1]] = 1
            return True
        #Step 2:排除非法以及障碍物节点    
        node_be_selected_1 = []
        for i in node_be_selected:
            if i[0]<0 or i[1]<0:
                continue
            if i[0]>=len(map_data) or i[1]>=len(map_data[0]):
                continue
            if map_data[i[0]][i[1]] == 0:
                node_be_selected_1.append(i)
        if len(node_be_selected_1) == 0:    # 如果无合法节点，则直接终止节点的选择
            return False
        #Step 3:计算节点与终点之间的距离，构建距离启发因子
        dis_1 = []    # 距离启发因子
        for i in node_be_selected_1:
            dis_1.append(((self.destination[0]-i[0])**2+(self.destination[1]-i[1])**2)**0.5)
        #Step 3.1:倒数反转
        for j in range(len(dis_1)):
            dis_1[j] = 1/dis_1[j]

        #Step 4:计算节点被选中的概率
        prob = []
        for i in range(len(node_be_selected_1)):
            p = (dis_1[i]**self.dis_imp) * (pher_data[y_1*len(map_data)+x_1][node_be_selected_1[i][0]*len(map_data)+node_be_selected_1[i][1]]**self.pher_imp)
            prob.append(p)
        #Step 5:轮盘赌选择某节点
        prob_sum = sum(prob)
        for i in range(len(prob)):
            prob[i] = prob[i]/prob_sum
        rand_key = np.random.rand()
        for k,i in enumerate(prob):
            if rand_key<=i:
                break
            else:
                rand_key -= i
        #Step 6:更新当前位置，并记录新的位置，将之前的位置标记为不可通过
        self.position = copy.deepcopy(node_be_selected_1[k])
        self.record_way.append(copy.deepcopy(self.position))
        map_data[self.position[0]][self.position[1]] = 1
        return True


# ## 标准蚁群算法
class ACO():
    def __init__(self,map_data,init,dest,max_iter = 100,ant_num = 100,pher_imp = 1,dis_imp = 10,evaporate = 0.7,pher_init = 8) -> None:
        '''
            Params:
            --------
                pher_imp : 信息素重要性系数
                dis_imp  : 距离重要性系数
                evaporate: 信息素挥发系数(指保留的部分)
                pher_init: 初始信息素浓度
        '''
        self.init = init    #初始点
        self.dest = dest    #目标点
        #Step 0: 参数定义及赋值
        self.max_iter = max_iter       #最大迭代次数
        self.ant_num  = ant_num        #蚂蚁数量
        self.ant_gener_pher = 1    #每只蚂蚁携带的最大信息素总量
        self.pher_init = pher_init #初始信息素浓度
        self.ant_params = {        #生成蚂蚁时所需的参数
            'dis_imp':dis_imp,
            'pher_imp': pher_imp
        }
        self.map_data = map_data.copy()        #地图数据
        self.map_length = max([self.map_data.shape[0], self.map_data.shape[1]])  #地图尺寸,用来标定蚂蚁的最大体力
        self.pher_data = pher_init*np.ones(shape=[self.map_data.shape[0]*self.map_data.shape[1],
                                            self.map_data.shape[0]*self.map_data.shape[1]])    #信息素矩阵
        self.evaporate = evaporate #信息素挥发系数
        self.generation_aver = []  #每代的平均路径(大小)，绘迭代图用
        self.generation_best = []  #每代的最短路径(大小)，绘迭代图用
        self.way_len_best = 999999 
        self.way_data_best = []     #最短路径对应的节点信息，画路线用  


        
    def run(self):
        #总迭代开始
        for i in range(self.max_iter):      
            success_way_list = []
            print('第',i,'代: ',end = '')
            #Step 1:当代若干蚂蚁依次行动
            for j in range(self.ant_num):   
                ant = Ant(max_step=self.map_length*3,pher_imp=self.ant_params['pher_imp'],dis_imp=self.ant_params['dis_imp'])
                ant.run(map_data=self.map_data.copy(),pher_data=self.pher_data,posi=self.init,dest=self.dest)
                if ant.successful == True:  #若成功，则记录路径信息
                    success_way_list.append(ant.record_way)
            print(' 成功率:',len(success_way_list),end= ' ')
            #Step 2:计算每条路径对应的长度，后用于信息素的生成量
            way_length_list = []
            for j in success_way_list:
                way_length_list.append(self.calc_total_length(j))
            #Step 3:更新信息素浓度
            #  step 3.1: 挥发
            self.pher_data = self.evaporate*self.pher_data
            #  step 3.2: 叠加新增信息素
            for k,j in enumerate(success_way_list):
                j_2 = np.array(j)
                j_3 = j_2[:,0]*self.map_length+j_2[:,1]
                for t in range(len(j_3)-1):
                    self.pher_data[j_3[t]][j_3[t+1]] += self.ant_gener_pher/way_length_list[k]
            #Step 4: 当代的首尾总总结工作
            self.generation_aver.append(np.average(way_length_list))
            self.generation_best.append(min(way_length_list))
            if self.way_len_best>min(way_length_list):
                a_1 = way_length_list.index(min(way_length_list))
                self.way_len_best = way_length_list[a_1]
                self.way_data_best = copy.deepcopy(success_way_list[a_1])
            print('平均长度:',np.average(way_length_list),'最短:',np.min(way_length_list))
        return self.way_len_best

    
    def calc_total_length(self,way):
        length = 0
        for j1 in range(len(way)-1):
            a1 = abs(way[j1][0]-way[j1+1][0])+abs(way[j1][1]-way[j1+1][1])
            if a1 == 2:
                length += 1.41421
            else:
                length += 1
        return length



# ## 精英蚁群算法    
class ACO_IMPROVED():
    def __init__(self,map_data,init,dest,max_iter = 100,ant_num = 100,pher_imp = 1,dis_imp = 10,evaporate = 0.7,pher_init = 8) -> None:
        '''
            Params:
            --------
                pher_imp : 信息素重要性系数
                dis_imp  : 距离重要性系数
                evaporate: 信息素挥发系数(指保留的部分)
                pher_init: 初始信息素浓度
        '''
        self.init = init    #初始点
        self.dest = dest    #目标点
        #Step 0: 参数定义及赋值
        self.max_iter = max_iter       #最大迭代次数
        self.ant_num  = ant_num        #蚂蚁数量
        self.ant_gener_pher = 1    #每只蚂蚁携带的最大信息素总量
        self.pher_init = pher_init #初始信息素浓度
        self.ant_params = {        #生成蚂蚁时所需的参数
            'dis_imp':dis_imp,
            'pher_imp': pher_imp
        }
        self.map_data = map_data.copy()        #地图数据
        self.map_length = max([self.map_data.shape[0], self.map_data.shape[1]])  #地图尺寸,用来标定蚂蚁的最大体力
        self.pher_data = pher_init*np.ones(shape=[self.map_data.shape[0]*self.map_data.shape[1],
                                            self.map_data.shape[0]*self.map_data.shape[1]])    #信息素矩阵
        self.evaporate = evaporate #信息素挥发系数
        self.generation_aver = []  #每代的平均路径(大小)，绘迭代图用
        self.generation_best = []  #每代的最短路径(大小)，绘迭代图用
        self.way_len_best = 999999 
        self.way_data_best = []     #最短路径对应的节点信息，画路线用  


        
    def run(self):
        #总迭代开始
        for i in range(self.max_iter):      
            success_way_list = []
            print('第',i,'代: ',end = '')
            #Step 1:当代若干蚂蚁依次行动
            for j in range(self.ant_num):   
                ant = Ant(max_step=self.map_length*3,pher_imp=self.ant_params['pher_imp'],dis_imp=self.ant_params['dis_imp'])
                ant.run(map_data=self.map_data.copy(),pher_data=self.pher_data,posi=self.init,dest=self.dest)
                if ant.successful == True:  #若成功，则记录路径信息
                    success_way_list.append(ant.record_way)
            print(' 成功率:',len(success_way_list),end= ' ')
            #Step 2:计算每条路径对应的长度，后用于信息素的生成量
            way_length_list = []
            for j in success_way_list:
                way_length_list.append(self.calc_total_length(j))
            #Step 3:更新信息素浓度
            #  step 3.1: 挥发
            self.pher_data = self.evaporate*self.pher_data
            #  step 3.2: 叠加新增信息素
            for k,j in enumerate(success_way_list):
                j_2 = np.array(j)
                j_3 = j_2[:,0]*self.map_length+j_2[:,1]
                for t in range(len(j_3)-1):
                    self.pher_data[j_3[t]][j_3[t+1]] += self.ant_gener_pher/way_length_list[k]
            # step 3.3: 精英蚂蚁路径信息素额外增加
            minidx = np.argmin(way_length_list)
            j = success_way_list[minidx]
            j_2 = np.array(j)
            j_3 = j_2[:,0]*self.map_length+j_2[:,1]
            for t in range(len(j_3)-1):
                self.pher_data[j_3[t]][j_3[t+1]] += self.ant_gener_pher/way_length_list[minidx]
            #Step 4: 当代的首尾总总结工作
            self.generation_aver.append(np.average(way_length_list))
            self.generation_best.append(min(way_length_list))
            if self.way_len_best>min(way_length_list):
                a_1 = way_length_list.index(min(way_length_list))
                self.way_len_best = way_length_list[a_1]
                self.way_data_best = copy.deepcopy(success_way_list[a_1])
            print('平均长度:',np.average(way_length_list),'最短:',np.min(way_length_list))
        return self.way_len_best

    
    def calc_total_length(self,way):
        length = 0
        for j1 in range(len(way)-1):
            a1 = abs(way[j1][0]-way[j1+1][0])+abs(way[j1][1]-way[j1+1][1])
            if a1 == 2:
                length += 1.41421
            else:
                length += 1
        return length

if __name__ == '__main__':
    map = '''
000000000000000000000000000000000000000000000000000000
011110111101111111111111111011111111111111011111111111
000000000000000000000000000000000000000000000000000000
111110111101111111111111111011111111111111011111111111
000000000000000000000000000000000000000000000000000000
011110111101111111111111111011111111111111011111111111
011110111101111111111111111011111111111111011111111111
000000000000000000000000000000000000000000000000000000
    '''
    map_data = []
    for _ in map.splitlines():
        line = _.strip()
        if len(line) > 0:
            row = []
            for __ in line:
                row.append(int(__))
            map_data.append(row)
    map_data = np.array(map_data)
    
    aco = ACO_IMPROVED(map_data=map_data,init=[6,0],dest=[6,53])
    print(aco.run())
