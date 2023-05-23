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
  4) A Fitness Score is given to each individual which shows the ability of an individual to “compete”. The individual having optimal fitness score (or near optimal) are sought.
  5) experiment result: 
     1st round: 2023-05-16 21:03:47,631 - INFO - utils.logging_stream_handler:77 - agent0, busy = 14646.0 second; odometer = 4540 meter. 
                     2023-05-16 21:03:47,631 - INFO - utils.logging_stream_handler:77 - agent1, busy = 15148.0 second; odometer = 4609 meter.
                     2023-05-16 21:03:47,632 - INFO - utils.logging_stream_handler:77 - agent2, busy = 14970.0 second; odometer = 4599 meter.
                     2023-05-16 21:03:47,632 - INFO - utils.logging_stream_handler:77 - agent3, busy = 14872.0 second; odometer = 4618 meter.
                     2023-05-16 21:03:47,632 - INFO - utils.logging_stream_handler:77 - agent4, busy = 15300.0 second; odometer = 4846 meter.
           
     2nd round: 2023-05-16 21:06:17,066 - INFO - utils.logging_stream_handler:77 - agent0, busy = 29344.0 second; odometer = 9132 meter. 
                    2023-05-16 21:06:17,066 - INFO - utils.logging_stream_handler:77 - agent1, busy = 29514.0 second; odometer = 8854 meter.
                    2023-05-16 21:06:17,066 - INFO - utils.logging_stream_handler:77 - agent2, busy = 30520.0 second; odometer = 9536 meter.
                    2023-05-16 21:06:17,066 - INFO - utils.logging_stream_handler:77 - agent3, busy = 29862.0 second; odometer = 9215 meter.
                    2023-05-16 21:06:17,066 - INFO - utils.logging_stream_handler:77 - agent4, busy = 30664.0 second; odometer = 9703 meter.
        
     3rd round: 2023-05-16 21:09:43,863 - INFO - utils.logging_stream_handler:77 - agent0, busy = 44438.0 second; odometer = 13737 meter.
                    2023-05-16 21:09:43,863 - INFO - utils.logging_stream_handler:77 - agent1, busy = 44080.0 second; odometer = 13399 meter.
                    2023-05-16 21:09:43,863 - INFO - utils.logging_stream_handler:77 - agent2, busy = 45300.0 second; odometer = 14049 meter.
                    2023-05-16 21:09:43,863 - INFO - utils.logging_stream_handler:77 - agent3, busy = 45382.0 second; odometer = 14151 meter.
                    2023-05-16 21:09:43,863 - INFO - utils.logging_stream_handler:77 - agent4, busy = 45668.0 second; odometer = 14330 meter.   
           
     4th round: 2023-05-16 21:11:15,662 - INFO - utils.logging_stream_handler:77 - agent0, busy = 60252.0 second; odometer = 18872 meter.
                    2023-05-16 21:11:15,662 - INFO - utils.logging_stream_handler:77 - agent1, busy = 58508.0 second; odometer = 17724 meter.
                    2023-05-16 21:11:15,662 - INFO - utils.logging_stream_handler:77 - agent2, busy = 60472.0 second; odometer = 18750 meter.
                    2023-05-16 21:11:15,662 - INFO - utils.logging_stream_handler:77 - agent3, busy = 59770.0 second; odometer = 18514 meter.
                    2023-05-16 21:11:15,662 - INFO - utils.logging_stream_handler:77 - agent4, busy = 60834.0 second; odometer = 19034 meter.
          
     5th round: 2023-05-16 21:12:17,360 - INFO - utils.logging_stream_handler:77 - agent0, busy = 75718.0 second; odometer = 23736 meter.
                    2023-05-16 21:12:17,360 - INFO - utils.logging_stream_handler:77 - agent3, busy = 75186.0 second; odometer = 23360 meter.
                    2023-05-16 21:12:17,360 - INFO - utils.logging_stream_handler:77 - agent1, busy = 73042.0 second; odometer = 22097 meter.
                    2023-05-16 21:12:17,360 - INFO - utils.logging_stream_handler:77 - agent4, busy = 75432.0 second; odometer = 23484 meter.
                    2023-05-16 21:12:17,360 - INFO - utils.logging_stream_handler:77 - agent2, busy = 75410.0 second; odometer = 23437 meter.
     Solved
  6) 加入了GA，但是对于session部分的tasklist存在一些问题，因为运行到后面会出现agent空转的情况，另外未想清楚如何解决去货品取到最后未达到capacity但是也需要把这一部分货品进行搬运的问题。 todo

# 20230519
工作总结：
1. 解决了AGENT空转问题，agent的计量表不能清零问题，以及tasklist不能正常导入问题。
2. 有待验证方法是否正确