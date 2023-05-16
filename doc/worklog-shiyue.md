[Geatpy: 遗传算法库](https://github.com/geatpy-dev/geatpy)

[Isaac sim 专栏](https://www.zhihu.com/column/c_1533191136755236864)

- GA in AGV 
Simultaneous scheduling of parts and automated guided vehicles in an FMS environment using adaptive genetic algorithm
https://link.springer.com/article/10.1007/BF02729112

- A genetic algorithm approach to the simultaneous scheduling of machines and automated guided vehicles
https://www.sciencedirect.com/science/article/abs/pii/S0305054896000615

# AI for game
[tag_Genetic_Algothm]
- Genetic Algorithm for game / Evolution Strategy.
- https://github.com/TsReaper/AI-Plays-FlappyBird
- Swam Intelligence, SI
- 启发式算法heuristic algorithm(没有在数学上证明是最优解的贪心算法，通常用来寻找可行解，以物拟人)
- 以仿自然体算法为主，主要有蚁群算法、模拟退火法、神经网络等。 
- 退火算法 (Simulated Annealing，SA) 


# Structure of the whole framework
objective function: 
1. The shortest distance: agent odometer, distance is determined by different algorithm, each algo res. [Improve ant algorithm can be considered to my novelty. ] 
2. The shortest working time: task fullfill time, it is determined by distance and moving speed. In the first experiment, I consider moving speed as a constant, but it is changed according to different items. 
3. Highest value: battery consumption, item price, item weight, item size
    Item weight, item size: They determine speed, and then speed determines battery consumption
[Consider value as a objective function can be my novelty]


# 20230515
1. 为什么实验结果在加入tasklist之后翻了5倍？ (整个tasklist被进行了5次): done total_number_or_session被定义成5，一次session表示整个仓库货物全部被取出来的一次结果，所以一共进行了5次，最后的结果也翻倍成5
2. agent put items into the cart, up to capacity, and then move.  one agent can pick up multiple items. Done
3. Strategy change. todo not home -> home, but home-> item1 location -> item2 location -> item3 location -> home.  Done

# 20230516
- GA Algorithm: https://www.geeksforgeeks.org/genetic-algorithms/
  1) Randomly initialize populations p
  2) Determine fitness of population
  3) Until convergence repeat:
        a) Select parents from population
        b) Crossover and generate new population
        c) Perform mutation on new population
        d) Calculate fitness for new population