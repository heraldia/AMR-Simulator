# 2022_1216_2044
# search 
 job shop scheduling problem
smart Warehouse github
smart Warehouse simulator github

# Web document
## 用python实现基于遗传算法求解带AGV的作业车间调度问题_码丽莲梦露的博客-CSDN博客_遗传算法机器调度 { 
https://blog.csdn.net/crazy_girl_me/article/details/123016551?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-123016551-blog-124243262.pc_relevant_3mothn_strategy_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-123016551-blog-124243262.pc_relevant_3mothn_strategy_recovery&utm_relevant_index=4
src
算法采用Bilge和Ulusoy等人设计的40个算例进行验证。
对此类问题做如下假设：

（1）机器旁出入缓冲区容量无限大；

（2）所有工件和AGV起始位置和加工完成回到的位置都在L/U站；

（3）不考虑AGV运输过程中的碰撞和故障；
} >

## 作业调度问题（jobshopschedulingproblem，JSSP）-合肥工业大学.ppt-全文可读 { 
https://max.book118.com/html/2018/0826/7133155110001144.shtm
Swam Intelligence, SI
p43: vehicle routing problem, VRP
p47: particle Swarm optimization 鸟飞行
} >

## 柔性作业车间调度问题（Flexible Job-shop Scheduling Problem, 简称为FJSP） - 腾讯云开发者社区-腾讯云 { good writing structure
https://cloud.tencent.com/developer/article/1635976

} >

## 干货 | Tabu Search求解作业车间调度问题(Job Shop Scheduling)-附Java代码_短短的路走走停停的技术博客_51CTO博客 {  1-dimension
https://blog.51cto.com/u_14328065/2847568

} >

## 作业车间调度JSP与遗传算法GA及其Python/Java/C++实现 - 腾讯云开发者社区-腾讯云 { 
https://cloud.tencent.com/developer/article/1590194?from=article.detail.1635976
### 转载 | 遗传算法求解混合流水车间调度问题（附C++代码） { 
https://mp.weixin.qq.com/s?__biz=MzI3NTkyODIzNg==&mid=2247484646&idx=1&sn=09e565fa0a7a7484dfe4721884ebd4c8&chksm=eb7c0125dc0b8833b5968f4e8d7bb8a0589ede08a86d57b5c7d93458fc7bf7b6ea47b368670e&scene=21#wechat_redirect
    good problem flow
混合流水车间调度问题（Hybrid Flow Shop Scheduling Problem,  HFSSP
若每阶段有且仅有一台加工机器，则称为经典流水车间调度问题Flow Shop Scheduling Problem, FSSP

} >


} >



# software
## Material Handling Simulation | FlexSim {  good
https://www.flexsim.com/material-handling-simulation/
very good video https://www.flexsim.com/videos/warehouse-optimization-and-digital-twin/ @17:20
Question: what rules are ready in FlexSim.
https://docs.flexsim.com/en/23.0/Reference/ProcessFlowObjects/SharedProperties/SharedProperties.html#change
![image](https://user-images.githubusercontent.com/75236407/208612073-858fa4c6-81e9-44cc-a701-784dc6cde0aa.png)

} >

## FlexSim AGV Simulation Software - Talumis { based on FlexSim
https://www.talumis.com/agv-simulation-software/

} >

## A simulation and control framework for AGV based transport systems - ScienceDirect { 
https://www.sciencedirect.com/science/article/pii/S1569190X21001271
good writing
Gazebo
There are many robot simulators such as Gazebo [9], V-REP [10], Webots [39] or Stage [40] that can be included in one or several robotic frameworks.
} >
## Isaac Sim - Robotics Simulation and Synthetic Data Generation | NVIDIA Developer {  on Unreal Engine
https://developer.nvidia.com/isaac-sim
Gazebo–Isaac Sim Connector, ROS 
todo-shiyue: think about what this can provide for our project?
### IsaacSim Unity3D — ISAAC 2020.1 documentation { 
https://docs.nvidia.com/isaac/archive/2020.1/doc/simulation/unity3d.html

} >


} >
## MoveIt Motion Planning Framework { 
https://moveit.ros.org/

} >
## ROS系统MoveIt玩转双臂机器人系列（一） { 
http://www.360doc.com/content/18/0621/10/10724725_764071624.shtml

} >





# dev
from Gantt_graph import Gantt

# youtube
## Inside Amazon's Smart Warehouse - YouTube { 
https://www.youtube.com/watch?v=IMPbKVb8y8s
- what is the human for?? todo-shiyue

} >

# github 2022_1217_0831
## cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing: In this project, we are trying to address this issue by developing a fully automated warehouse management that will minimize the drawbacks while improving efficiency and profitability. We are implementing a warehouse management system which consists two types of robots; robots arms to handle loading/unloading of goods, automated guided vehicles to transport goods inside the warehouse. Also, an online shopping portal to make the purchases from the warehouse. { 
https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing
The warehouse has two base stations, the delivery post and receiving post, to deliver goods to the customers and receive any stocks to the warehouse respectively.
minimizing the travel time.
} >


## rodriguesrenato/warehouse_robot_simulation: A full simulation of a warehouse autonomous mobile robot that handles Orders and performing picking and delivery Products in a warehouse in Gazebo simulator. { 
https://github.com/rodriguesrenato/warehouse_robot_simulation
Gazebo game-level
} >

## semitable/robotic-warehouse: Multi-Robot Warehouse (RWARE): A multi-agent reinforcement learning environment { 
https://github.com/semitable/robotic-warehouse
The environment is configurable: it allows for different sizes (difficulty), number of agents, communication capabilities, and reward settings (cooperative/individual).  good
Agents have been trained with the SEAC algorithm [2].  todo-shiyue
Collisions
Custom layout // so good!!!
 title={Benchmarking Multi-Agent Deep Reinforcement Learning Algorithms in Cooperative Tasks}, todo learn this, 2-d
} >

## RoBorregos/smart-factory: EAIBot Smart Factory { 
https://github.com/RoBorregos/smart-factory
ROS
} >

## LyapunovJingci/Warehouse_Robot_Path_Planning: A multi agent path planning solution under a warehouse scenario using Q learning and transfer learning.🤖️ { 
https://github.com/LyapunovJingci/Warehouse_Robot_Path_Planning
Q-learning, gif 2d
} >

## abel-gr/warehouse-robot: A swarm of autonomous robots that manage a warehouse's orders and boxes in a collaborative and efficient way. Simulated in Unity and Coppelia. { much domain knowledge, 3d unitCoppeliaSim y
https://github.com/abel-gr/warehouse-robot
~ unity !!!! amazing todo-shiyue
mostly same as my thought
    In addition, they also stop giving priority to the robots that they detect on their right.
    For example, the robotic arm is locked in all states except in the PickingUp state. The robot can only receive new tasks in the Available state. Also, in the PickingUp, RampGoingDown, Unloading, and RampGoingUp states, the rotation of the robot and wheels is automatically locked. 
Coppelia: https://github.com/abel-gr/warehouse-robot/wiki#realistic-simulation
                /CoppeliaSim /
We also have designed a website where the warehouse orders are stored, and a human worker can add manually and with his/her own voice orders to be processed by the robot swarm.
minimize the total time of the collection of boxes from the warehouse 
When the training mode is enabled after a certain number of orders are processed by the robots, `the weights of the formula used to determine which robot is the most suitable for picking an order are modified in each iteration.`
what is node? 2 folds meaning.
Head-on collisions cannot occur because all nodes have a single direction of driving. // node == robot

warhouse_node.cs // node is the every shelf
It begins to go towards him and once he arrives he changes his status to Available because now the robot is located in one of the nodes of the warehouse.
Warehouse_orders.cs
The calculation of the formula includes values such as the distance to the order, the number of orders processed and the capacity of each robot, and all the values have certain weights that are calculated in the Warehouse_training.cs script.
Warehouse_shelf.cs
Each shelf script has two Warehouse_node.cs scripts associated to it, of the nodes that are at the left and the right of that shelf, allowing the robots to know the node coordinates of the shelf where is the box that must be picked up.
it will be able to move towards a value of X (or Z depending on the variable) that is greater than the one it is, that is, in a positive direction. If it is false, it can only move in the negative direction. In this way, lane generation is also automated and works perfectly.

algo:
    OptimalRoute.cs
        It has a recursive backtracking algorithm to calculate the optimal path between two warehouse nodes. It has various conditions to prune branches so it runs fast.
    warehouse_training.cs
        In case that the container is full, the robot itself will set the OnWayToDrop status and go to the box unloading area. Otherwise, it will remain in Available until the Warehouse_orders.cs script assigns it another box to collect, and the process will start again. //
        In each iteration, the weights are modified with the inverse of the time it took for all the robots to process a certain number of orders specified in the ordersPerIteration variable.



src: https://github.com/abel-gr/warehouse-robot/wiki/Unity-simulation#Warehouse_nodecs
https://github.com/abel-gr/warehouse-robot/tree/master/Simulation/Unity/Warehouse%20simulation/Assets
           //
} >

## wh200720041/warehouse_simulation_toolkit: A simulation toolkit for ground robot AGV in warehouse environment, including tutorials for robot navigation and localization {  ros
https://github.com/wh200720041/warehouse_simulation_toolkit

} >

# paper
## Shiyang Huang- Google Scholar{ 
https://scholar.google.com/citations?user=3JnikiwAAAAJ&hl=en

} >

## Optimization of job shop scheduling with material handling by automated guided vehicle Shiyang Huang Iowa State University { 
chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://core.ac.uk/download/pdf/212843913.pdf
global optimal makespan 
a new visualization method extending traditional Gantt charts is proposed to reflect the interaction between AGV movements and job operations. 
estimated processing times
} >

chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://keep.lib.asu.edu/_flysystem/fedora/c7/116746/Huang_asu_0010N_14128.pdf
## 基于AGV的物流作业车间调度优化_码丽莲梦露的博客-CSDN博客 { 
https://blog.csdn.net/crazy_girl_me/article/details/124243262
https://www.proquest.com/openview/9191c507f8e48c05fc9b5b58684b196d/1?pq-origsite=gscholar&cbl=51908
Shop Scheduling with Material Handling (JSSMH) 

} >


## Design and Development of an automated Robotic Pick & Stow System for an e-Commerce Warehouse { 
https://www.researchgate.net/publication/314283198_Design_and_Development_of_an_automated_Robotic_Pick_Stow_System_for_an_e-Commerce_Warehouse

} >

## Multi-AGV Tracking System Based on Global Vision and AprilTag in Smart Warehouse | SpringerLink { 
https://link.springer.com/article/10.1007/s10846-021-01561-5?utm_source=xmol&utm_medium=affiliate&utm_content=meta&utm_campaign=DDCN_1_GL01_metadata

} >

# 2022_1225_1757
# path finding algorithm

# path-planning · GitHub Topics { 
https://github.com/topics/path-planning?l=python&o=desc&s=updated
more to explore
} >

## zhm-real/PathPlanning: Common used path planning algorithms with animations. { many algorithms | best
https://github.com/zhm-real/PathPlanning
[we need the shortest path.]
- four Chinese contributors
    https://www.linkedin.com/in/huiming-zhou-03500b145/
    https://www.linkedin.com/in/yue-qi/
5th reading 
} >

## zhm-real/MotionPlanning: Motion planning algorithms commonly used on autonomous vehicles. (path planning + path tracking) { interesting
https://github.com/zhm-real/MotionPlanning
visualization of various vehicles
} >


## AtsushiSakai/PythonRobotics: Python sample codes for robotics algorithms. { very complete set of algorithms and tools | 94 contributors | best
https://github.com/AtsushiSakai/PythonRobotics
3rd reading 
many algorithms, pathplanning is one of many categories.
This is a 2D navigation sample code with Dynamic Window Approach.
good for us: avoiding an obstacle
    Dynamic Window Approach
    D* algorithm
} >
## RuslanAgishev/motion_planning: Robot path planning, mapping and exploration algorithms { 
https://github.com/RuslanAgishev/motion_planning
2nd reading
The algorithm is provided not only for an ego-vechicle but also for a group of robots.
as well as for drone in 3D environment
RTT algorithm
} >


## prchinmay/robot_waiter: A path planning and control method is developed for the scenario of a non-holonomic robot serving food in a restaurant. { a paper, 
https://github.com/prchinmay/robot_waiter
[we need the shortest path.]: The path planning algorithm used is PRM*, where a semi-random point sampling algorithm is used. Graph search is performed by the Dijkstra algorithm, after which b-splines is used to smoothen the path.
4th reading
good: design map in png.
} >

## jannikmi/extremitypathfinder: python package for fast shortest path computation on 2D polygon or grid maps {  very good
https://github.com/jannikmi/extremitypathfinder
1st reading
a good team management.
https://extremitypathfinder.readthedocs.io/en/latest/1_usage.html
find_shortest_path
} >

## 【规划】机器人规划算法总结_笑扬轩逸的博客-CSDN博客_机器人规划包括那三个层次 { 
https://blog.csdn.net/yuxuan20062007/article/details/86787995?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-2-86787995-blog-110368020.pc_relevant_3mothn_strategy_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-2-86787995-blog-110368020.pc_relevant_3mothn_strategy_recovery&utm_relevant_index=3
psudo code
} >

## iory/scikit-robot: A Flexible Framework for Robot Control in Python { irrelevant
https://github.com/iory/scikit-robot
robot body, motion planning

} >

# pathfinding-algorithms · GitHub Topics { 
https://github.com/topics/pathfinding-algorithms?l=python

} >

## gavincangan/multiagent-pathfinding: Conflict-based search for multi-agent path finding { 
https://github.com/gavincangan/multiagent-pathfinding
good 
} >
多个扫地机器人，这个点子很有research 启发。

