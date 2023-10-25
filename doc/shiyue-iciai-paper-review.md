Congratulations on the first draft.

https://github.com/heraldia/AMR-Simulator/compare/main...review-paper
// Symbol Description:
/*ability*/ means to remove word "ability";
/*+s*/ means to append a letter 's';
/*a=>an*/ means to replace "a" with "an";
/*1e1 up to -10.: what is this meaning? */ means giving some comments to the part before : 
//
// ANY PITFALLS BEING POINTED HERE MEANS THAT IT IS HIGHLY POSSIBLE A SIMILAR TYPE OF PITFALLS HIDDEN IN THE MANUSCRIPT. SO PLEASE TAKE YOUR TIME TO SEEK THEM OUT.
// ----------------------------------------------------------

# Iterative Task Allocation Optimization using Heuristic and Local Search Algorithms with A Novel Simulator: Warehouse Autonomous Mobile Robot // title is so cool
SHIYUE HU
Graduate School of Information, Production and Systems, Waseda University
SHIGERU FUJIMURA
Graduate School of Information, Production and Systems, Waseda University
YUNFEI, FENG
Walmart Inc., Bentonville, AR, /*+ USA */ 72712

# ABSTRACT
Industry 4.0 /*transformed ->transforms*/ warehouse operations with automation and Autonomous Mobile Robots (AMRs), enhancing efficiency and cost-effectiveness. 
The Warehouse Autonomous Mobile Robot /*WAMR -> (WAMR) */ Simulator optimizes AMR systems for peak performance in warehouses, allowing direct user interaction and customized simulation environments. 
This paper proposes a novel task allocation methodology using GA and PSO in conjunction with the WAMR Simulator to /*enhance -> boost*/ warehouse operational efficiency and productivity. 
The proposed method generates and distributes optimized item task lists through scheduling algorithms within the simulator framework. 
/*The -> Hereby, the */ iterative optimization process ensures efficient task distribution, thereby improving warehouse operational efficacy. 
/*The paper -> We */ outlines the simulator's architecture, /*the -> a*/ proposed task allocation method, and /*the -> multi-aspect */ significant improvement/*s*/ in warehouse operations, supported by rigorous experimentation. 
/*This -> Furthermore, t*/ work underscores the potential of integrating advanced simulation frameworks with intelligent task allocation strategies in propelling warehouse operations to new efficiency frontiers.

// Overall, all sentence in the Abstract section are in the same structure, subject- verb.-object, we need more variety in style.
// think about whether we need emphasize scalability and flexibility and extendable? 

CCS CONCEPTS ¥ 
Keywords: Autonomous Mobile Robot, Simulator, Task allocation, Scheduling algorithm

# 1 INTRODUCTION
  The rise of Industry 4.0 has transformed warehouse operations by implementing automation and Autonomous Mobile Robots (AMRs). These AMRs offer a highly adaptable and scalable solution for material handling and transportation needs. To ensure maximum efficiency and cost-effectiveness, /*the -> a*/ Warehouse Autonomous Mobile Robot Simulator (WAMR Simulator) has been developed to optimize AMR systems. As a global platform for warehouse robotics operations, the WAMR Simulator specializes in transportation planning and boasts several unique benefits compared to other simulators. 

  The WAMR Simulator offers two primary features: it is lightweight and highly customizable. By eliminating the need for third-party software, users can directly arrange the factory layout, define robot performance and task completion methods, and specify desired results quickly. The simulator is also customizable, allowing users to add, modify, or remove components and experiment with different operational settings to find the optimal configuration for their warehouse operations. 
  Efficient allocation of tasks to Autonomous Mobile Robots (AMRs) can significantly boost warehouse productivity. However, task allocation in a warehouse is a complex problem that requires advanced scheduling algorithms. Using an AMR simulator can help develop and test robust task allocation algorithms to improve operational efficiency and productivity. This paper proposes a novel task allocation method that utilizes Genetic Algorithm (GA) and Particle Swarm Optimization (PSO) and their improved algorithms for optimization by combining them with the WAMR Simulator, leading to improved operational efficiency and productivity.
  Firstly, this paper presents the WAMR Simulator, a Python-based simulation platform for warehouse robotics operations. The simulator is designed for the transportation planning of items according to different task requirements and offers a scalable, customizable, and lightweight solution for warehouse management. The WAMR Simulator eliminates the need for third-party software for constructing the warehouse environment, creating robot and factory equipment models, and encoding the assembly of factory components.
  The WAMR Simulator is utilized within a task allocation method to optimize operations. Customers submit orders, which are categorized into item task lists based on delivery times and sent to the warehouse management system. Warehouse robots, or agents, have a limited load capacity, so creating an agent task for each agent before each trip is crucial. An agent's trip involves collecting goods from assigned areas until they reach their load capacity, delivering them to various numbered destinations, and returning to the starting point to decide if they need to recharge. The agent task list is a comprehensive list of tasks that all agents must accomplish.
  Secondly, this paper introduces a task allocation method in the WAMR Simulator that uses scheduling algorithms for optimization. The method generates item task lists and allocates them using the simulator. A fitness value is produced and sent to the GA for selection, mutation, and crossover to create multiple generations of item task lists. This optimization process results in an efficient distribution of tasks in the warehouse, leading to better warehouse operations. PSO and its improved algorithms use similar optimization processes for optimal allocation. 
  The paper is structured as follows: Section 2 provides a literature review of related work in the field. Section 3 provides a detailed description of the WAMR Simulator, including its key features and advantages. Section 4 presents the task allocation method implemented in the simulator and the use of several scheduling algorithms for optimization. Section 5 presents the experiment results. Finally, Section 6 /*gives -> draws*/ a conclusion.
# 2 LITERATURE REVIEW
  Mobile robots have transformed warehouse operations. In 1997, Alami and colleagues introduced a "plan-merging paradigm" for multi-robot collaboration in the WAMR Simulator [1]. However, this approach does not fully address the distinct challenges and constraints of a warehouse setting. Kim and co-authors (2020) recently developed a control framework for the OWMR robot [2]. Nevertheless, their investigation is limited to the OWMR model, which may not be applicable to warehouses employing alternative robots. Zghair and Al-Araji's 2021 survey examines the control systems of autonomous mobile robots over the past decade, stressing their significance in enabling independent robots [3]. Alternatively, Shetty, Sah, and Chung (2020) proposed a vehicle routing-based method that surpasses traditional techniques for optimal route planning in manual order-picking systems [4]. However, their study does not incorporate the use of a simulator to simulate the pick-up and delivery process. 
  The warehouse industry has seen innovative approaches to enhance efficiency. Dou et al. (2015) combined GA-based task scheduling with reinforcement learning-based path planning for mobile robots to improve intelligent warehouse efficiency [5]. However, this method may not be suitable for highly dynamic operations. To address this, the WAMR Simulator allows testing of task allocation algorithms under varied conditions. Tsang et al. (2018) presented a warehouse multi-robot automation system focusing on task allocation and path planning, but their approach may not be practical for real-time task allocation in large-scale warehouses [6]. Karami et al. (2020) discussed task allocation for human-robot collaboration scenarios [7], while Li et al. (2018) focused on path planning for mobile robots [8]. However, neither addressed the critical aspect of warehouse operations - task allocation. In contrast, the WAMR Simulator provides a comprehensive solution for path planning and task allocation in a warehouse setting. Chatzisavvas et al. (2022) proposed an algorithm for optimal pathfinding that considers the energy consumption factor and selects the most efficient route [9]. However, this approach does not consider task allocation. Ganbold et al. (2020) introduced a simulation-based optimization method for warehouse worker assignment, but this approach only considers human workers and does not include the use of robots in the warehouse [10]. 
  Previous research explored the potential of scheduling algorithms to optimize task allocation in warehouse operations using AMRs. To accomplish this, the WAMR Simulator was developed as a lightweight and customizable simulation platform specifically designed for warehouse robotics operations. Its comprehensive solution considers the complexities and constraints of a fully automated warehouse environment. By combining the results of the WAMR Simulator with several scheduling algorithms, the paper also presents an optimal solution for task allocation. 
# 3 DESCRIPTION/*S*/ OF THE WAMR SIMULATOR 
  The WAMR Simulator is a lightweight and customizable simulation platform explicitly designed for warehouse robotics operations. It offers many features and benefits, including quickly obtaining results without visualization, high scalability and customization, and a user-friendly architecture. This simulator is an asset for organizations looking to enhance the efficiency and effectiveness of their warehouse robotics systems. Providing users with the right tools and flexibility to simulate and optimize their warehouse operations can improve their performance. In the following section, this article explains in detail the various components of the system and the default approach for completing tasks, which involves assigning one robot per suitable task.
3.1 Robot
  The Agent Manager module is responsible for regulating the behavior and status of robots by maintaining a list. The class is designed using the Singleton pattern, which guarantees that only one class instance is created.
  The Agent Manager module efficiently handles the management of warehouse robots, providing them with unique IDs and arranging them into distinct lists. The module keeps track of the robots' statuses by adding or removing their IDs from state lists. Additionally, it employs statistical methods to compute each robot's cumulative distance and work time. To suit individual needs, users can easily modify the simulator's output. 
  This module's critical feature is defining the robot charging process. Macro regulation involves changing the robot's ID in state lists for charging. The robot's predetermined charging method carries out the procedure at a constant default rate. The charging time is calculated as follows: 
  /*
time to charge=(agent max?battery-agent current battery)/(charging speed)
duration of changing = (agent battery capacity - agent current remaining battery level) / charging rate
*/
  When a robot /*enters -> turns into */ the charging state, it is moved to the pausing state list. Upon charging completion, the robot battery level is updated to its maximum capacity, and the robot is transferred from the pausing state list to the idle state list. 
  The simulator manages the robot's charging behavior by monitoring its battery level and setting a threshold value. The threshold value is defined by a pre-experiment in the path planning algorithm that the user wishes to use. If the battery level is below the threshold, the robot is set to charge, and its ID is displayed. Once charging is complete, the robot is moved to the idle state list. The robot starts its task without charging if the battery level is above the threshold. This method helps conserve the robot's resources and minimizes energy waste. 
  Another method is available to check all robots in case the home and charge station are not in the same location in the future. Idle robots with less than full battery levels are sent to charge with a lower priority than robots with tasks. This ensures maximum charging station utilization and reduces robot waiting to charge queues. The whole process is shown in Figure 2. 

/* Figure 2: Process of charging before tasks start   */  
//   ALL FIGURE CAPTIONs SHOULD BE IN A SMALLER FONT SIZE. 

3.2 Item
  The Item Manager module oversees the movement and tracking of all items within the system. Like the Agent Manager module, it utilizes a list-based system to manage many items effectively. Before each task, an empty list is generated, and all items are registered. Individual items are retrieved from the list throughout the task, and their status is updated accordingly. 
  Before defining this module's functions, the constructor initializes the item list. If the initial list is provided, it copies that list. Otherwise, it initializes an empty list. By default, an empty item list is established firstly to facilitate the control of item transportation by adding and removing items. The module encompasses three distinct functions: 
1.	Adding an item: This function is employed before the start of a task to register all items in the item list, providing a comprehensive record of all item information. 
2.	Picking an item: During task execution, this function assigns items to be transported by each robot. Once an item is selected, it's removed from the list. 
3.	Item status processing: This feature utilizes the item status update method defined in the Item module. When an item is chosen for transportation, its status goes from "In-stock" to "Reserved". After completing transport, the item's status changes from "Reserved" to "Processed". Unlike the Agent Manager module, the Item Manager module's status changes occur all at once instead of cycling through.
  The Item Manager module plays a crucial role in monitoring the transportation and status of items within the system. Using a list-based approach and offering functions of adding an item, picking an item, and item status processing, it effectively manages the dynamic item environment and ensures task execution smoothly. The whole working process of Module Shelf, Item, and Item Manager is shown in Figure 3.

Figure 3: The complete working process with the Module Shelf, Item, and Item Manager.
3.3 Task Completion
  The Session module includes activities before, during, and after a task. At the start of a task, one item is selected from the list waiting for transportation. An idle robot is called upon from the Agent Manager module and paired with the selected item. Before starting a task, the robot's battery power must be checked using the Agent Manager module's battery level check method. If the robot needs to be charged, it should be charged first. Once charging is complete, the Agent Manager and Item Manager modules update their respective robot and item status lists. The robot is transferred from the Idle list to the On-duty list, while the item is moved from the In-stock list to the Reserved list. Once the robot finishes a task, the Task module displays the time and distance traveled, and updates the robot's and item's status. The information is added to a list and saved in a file for analysis. The Session module repeats the process for each item waiting for transportation, and the Agent Manager outputs the results using a statistical method. The simulator generates data on each robot's cumulative distance traveled and total working time, which can be customized user's requirements. The whole process of finishing transportation is shown in Figure 8. 
  To simulate a factory transportation scenario, the simulator uses multi-threading for robots, but this increases their chances of collision. A collision-checking method is established to prevent this. If a collision is detected, one robot must stop and make way. The robot closest to the destination gets priority. Once the pausing robot returns to the On-duty list, the giveaway rule can be defined per user requirements. The exact process of the collision-checking method is shown in Figure 9. 
  
  // Figure 8: Session module working process,  // font size is too small. We need restructure it.
  
  // Figure 9: /* Change -> Move */ one robot from On-duty list to Pausing list.
  // Figure 9: /* Change -> Move */ the robot from Pausing  list to On-duty list.
  // The same in the Figure 8.
  Figure 9: Collision-checking method flowchart
TASK ALLOCATION OPTIMIZATION BASED ON THE WAMR SIMULATOR
Problem Description
  The WAMR Simulator is a tool for optimizing settings and generating customized results. Using it, an experiment developed an optimal solution for coordinating item delivery to destinations with autonomous mobile robots. The experiment includes a task allocation system to optimize task sequences in a simulated warehouse environment. 
  When receiving customers ' orders, the warehouse displays information about items like storage location, destination, weight, and priority. A list of item tasks is created based on customer orders and an agent selects items from it based on load capacity. All selected items are combined into one task known as an agent task. Once an agent task is done, agents get a new one until all items are transported. The simulator calculates the distance and time worked by agents. However, the sequence of items on the item task list may not be optimal based on the working time and cumulative distance traveled by the agent. Therefore, an experiment will add task allocation optimization to obtain an optimal result for the item task list.

Figure 10: The flow chart of the experiment combined simulation and task allocation optimization
  Illustrated in Figure 10 is the process of creating an optimized item task list. This involves the automatic generation of an item task list that considers the priority of customer orders. These items are then assigned to individual agents as several agent tasks. Once all the items have been transported by the agents, the system calculates a fitness value to determine if the optimal solution has been achieved. The optimal solution is obtained if the value is optimal or the maximum number of iterations has been reached. However, if the value is not optimal, the item task list is continually optimized with specific algorithms. One of the most important factors is the fitness value, which is considered as the objective. The fitness value is shown below as the experiment's objective function: 
  Fitness value=?D+?T+?L=?·?P_i ?max?(c_i-p_i,0)+?T+?L
D: the penalty of due time, D=?·?P_i ?max?(c_i-p_i,0)
  P_i:Priority of item i. It determines the importance or urgency of the item i.
  c_i:Completion time of item i. 
  p_i:Due time of item i. It it the time by which the item should ideally be completed transportation. 
  Each item's due time is fixed 
T: agent working time
L: agent working distance
  ?, ? and ?:hyperparameter
  In this function, the fitness value is a weighted sum of three components: the penalty due to time D, all agentsÕ cumulative working time for one item task list T, and all agentsÕ working distance for one item task list L. The weights ?, ? and ? are hyperparameters that determine the relative importance of each component in the overall fitness value. The expression max?(c_i-p_i,0) calculates the delay for item i. If c_i (completion time) is longer than p_i (due time), there is a delay, and the difference (c_i-p_i) represents the extent of that delay. If c_i is less than or equal to p_i, the item is completed on time or early, and there is no delay. Using the max function ensures that the penalty is only applied when there is a delay. If an item is completed before or exactly at its due time, the penalty for that item is 0. The result is closer to the optimal value if the fitness value is less. 
Experiment Result

Figure 11: Minimum objective function value of the population of each iteration in the small-scale layout

Figure 12: Minimum objective function value of the population of each iteration in the large-scale layout
  In the experiment, two different kinds of scale factory layouts are used in the simulator, considered small-scale and large-scale layouts. The iteration of the small scale is set to 60, and the large scaleÕs is 105. Each iteration has 20 item task lists. The figure only shows the minimum fitness value in each 20-item task list.
  Figure 11 shows the fitness value decreasing with iterations. A* algorithm is used for path planning, and four algorithms are compared - hybrid GA, GA, hybrid PSO, and PSO. GA is more effective for small-scale factory layouts. PSO and hybrid PSO reach an optimal result after 20 and 23 iterations, respectively. GA and hybrid GA can achieve smaller optimal fitness values than PSO and hybrid PSO by 60 iterations.
  Figure 12 displays four algorithms' minimum objective function values in the large-scale layout. It shows that hybrid GA and hybrid PSO have better optimization results compared to PSO and GA. The fitness value of GA and PSO stops decreasing after the 11th and 15th iterations, indicating a limited optimization effect. This differs slightly from the results shown in Figure 12.
  /*+ In total, */ 40 experiments were conducted to analyze the stability of different scheduling algorithms in small-scale and large-scale layouts. Two box plots demonstrate the stability of algorithms.
  The box plots are generated for the data to represent each algorithm's spread and stability visually. 
// Figure 17, it is better for y-axis, using 160,000 or 160k if possible. 
Figure 17. Stability of optimal solutions for multiple runs of GA and PSO in the small-scale and large-scale layout
  In the large-scale data, the box plot visually confirms that GA appears to be the most stable, with a compact interquartile range (IQR) and no outliers. The hybrid GA algorithm has a wide IQR, indicating that it is less stable than the others. PSO seems the most stable in the small-scale data, and hybrid GA is the least stable algorithm. 
CONCLUSION
The growth of e-commerce has led to a rise in the number of warehouses worldwide.  
/*  T -> Alongside, t*/his has created challenges in managing these warehouses effectively /*. -> , */
/* The main issue is how to organize the tasks required to retrieve items efficiently. 
->
One of which is how to organize the tasks required to retrieve items efficiently. 
*/

This involves coordinating a detailed item task list that specifies which items must be delivered to which destination. 
/* Researchers ? Do you mean us or other researcher? if us, -> We */ have developed a strategy for autonomous mobile robots designed for a simulated warehouse environment to address this. 
This environment has various items arranged methodically on shelves. 
As orders come in, the system processes each order based on its alignment with the items on the shelves. 
This creates a comprehensive item task list that covers all the orders related to the shelves. 
The approach ensures that tasks are distributed fairly among the robots, considering their carrying capacity and ability to transport items efficiently. 

// Overall, all sentence in the CONCLUSION section are in the same structure, subject- verb.-object, we need more variety in style.

// The current CONCLUSION section just restate the problem and solution. We can summary those in two sentences and emphasize the importance of our work in the academic community and our future work.


# REFERENCE
[1]	R. Alami, S. Fleury, M. Herrb, F. Ingrand, and S. Qutub, ÒOperating a large fleet of mobile robots using the plan-merging paradigm,Ó 1997. [Online]. Available: https://hal.laas.fr/hal-01979708
[2]	C. Kim, J. Suh, and J. H. Han, ÒDevelopment of a hybrid path planning algorithm and a bio-inspired control for an omni-wheel mobile robot,Ó Sensors (Switzerland), vol. 20, no. 15, pp. 1Ð22, Aug. 2020, doi: 10.3390/s20154258.
[3]	N. A. K. Zghair and A. S. Al-Araji, ÒA one decade survey of autonomous mobile robot systems,Ó International Journal of Electrical and Computer Engineering, vol. 11, no. 6. Institute of Advanced Engineering and Science, pp. 4891Ð4906, Dec. 01, 2021. doi: 10.11591/ijece.v11i6.pp4891-4906.
[4]	N. Shetty, B. Sah, and S. H. Chung, ÒRoute optimization for warehouse order picking operations via vehicle routing and simulation,Ó SN Appl Sci, vol. 2, no. 2, Feb. 2020, doi: 10.1007/s42452-020-2076-x.
[5]	J. Dou, C. Chen, and P. Yang, ÒGenetic Scheduling and Reinforcement Learning in Multirobot Systems for Intelligent Warehouses,Ó Math Probl Eng, vol. 2015, 2015, doi: 10.1155/2015/597956.
[6]	Kam Fai Elvis Tsang, Yuqing Ni, Cheuk Fung Raphael Wong, and Ling Shi, A Novel Warehouse Multi-Robot Automation System with Semi-Complete and Computationally Efficient Path Planning and Adaptive Genetic Task Allocation Algorithms. IEEE, 2018. Accessed: Jul. 18, 2023. [Online]. Available: https://ieeexplore.ieee.org/document/8581092
[7]	H. Karami, K. Darvish, and F. Mastrogiovanni, ÒA Task Allocation Approach for Human-Robot Collaboration in Product Defects Inspection Scenarios,Ó Sep. 2020, [Online]. Available: http://arxiv.org/abs/2009.06423
[8]	C. Li, Z. Wang, C. Fang, Z. Liang, Y. Song, and Y. Li, ÒAn Integrated Algorithm of CCPP Task for Autonomous Mobile Robot under Special Missions,Ó 2018.
[9]	A. Chatzisavvas, P. Chatzitoulousis, D. Ziouzios, and M. Dasygenis, ÒA Routing and Task-Allocation Algorithm for Robotic Groups in Warehouse Environments,Ó Information (Switzerland), vol. 13, no. 6, Jun. 2022, doi: 10.3390/info13060288.
[10]	O. Ganbold, K. Kundu, H. Li, and W. Zhang, ÒA simulation-based optimization method for warehouse worker assignment,Ó Algorithms, vol. 13, no. 12, Dec. 2020, doi: 10.3390/a13120326.
AuthorsÕ background
Your Name
Title*
Research Field
Personal website
Shiyue Hu
# last page
/* Phd -> Ph.D.*/ candidate

Simulation, Scheduling optimization

Shigeru Fujimura
Professor
Software, Intelligent informatics, Control and system engineering
https://w-rdb.waseda.jp/html/100000682_en.html
Yunfei Feng
Staff Machine Learning Engineer, Tech Lead
Indoor localization, computer vision, /*machine learning, deep learning -> system integration*/, sensor fusion on smart devices, smart buildings and smart systems
https://scholar.google.com/citations?user=2d0HxpIAAAAJ&hl=en





// We need enlarge font size in figures. e.g. Figure 11. 1 2 3 ...            We can enlarge font size and only mark 0, 10, 20, 30 ....
// We might need more reference, better to be around 16 references.


----------------

# 2023_1024_2028 
Authors' background:
Simulation, Scheduling optimization // all three author either follow title style or normal lowercase style.
e.g.
Indoor localization, computer vision, machine learning, deep learning, sensor fusion on smart devices 
or 
Indoor localization, Computer vision, Sensor fusion on smart devices, smart buildings and smart systems

Indoor localization, computer vision, machine learning, deep learning, sensor fusion on smart devices -> Indoor localization, computer vision, sensor fusion on smart devices, smart buildings and smart systems


# Abstract
Industry 4.0 transforms warehouse operations with automation and Autonomous Mobile Robots (AMRs), enhancing efficiency and cost-effectiveness. 
The WAMR Simulator optimizes AMR systems for peak performance in warehouses. 
It allows direct user interaction and customized simulation environments, showing scalable, flexible, and extendable features. 
/*Therefore, t -> T*/his paper proposes a novel task allocation methodology using GA and PSO in conjunction with the WAMR Simulator to boost warehouse operational efficiency and productivity. 
The proposed method generates and distributes optimized item task lists through scheduling algorithms within /*the -> a*/ simulator framework. 
Hereby, the iterative optimization process ensures efficient task distribution, /*thereby*/ improving warehouse operational efficacy. 
We outline the simulator's architecture, a proposed task allocation method, and multi-aspect significant improvements in warehouse operations, /*supported -> validated */ by rigorous experimentation. 
Furthermore, the work underscores the potential to integrate advanced simulation frameworks with intelligent task allocation strategies to propel warehouse operations to new efficiency frontiers.

# 5. CONCLUSION
The growth of e-commerce has led to a rise in the number of warehouses worldwide. 
Alongside, this has created challenges in managing these warehouses effectively, one of which is how to organize the tasks required to retrieve items efficiently. 
Coordinating a detailed task list for delivering items to their respective destinations is crucial. 
To address this, we have developed a strategy for autonomous mobile robots that are designed for a simulated warehouse environment. 
In this environment, items are arranged methodically on shelves, and the system processes each order based on its alignment with the items on the shelves. 
This creates a comprehensive item task list that covers all the orders related to the shelves. 
Our approach ensures that tasks are distributed fairly among the robots, considering their carrying capacity and ability to transport items efficiently. 
There are some /*areas of improvement that can be made to -> room to improve on / the current simulator. 
/* One suggestion is -> We can further try */ to replace the fixed collision threshold of one unit with a /*dynamic -> adaptive*/ threshold /*that considers -> in regards with */ the speed of the robots. 
Another potential improvement is to use the WAMR Simulator /*to solve -> for a scenario similar with the */ Knapsack problem in a targeted manner.

