# A use-case
Is there a necessary cold start or run 7/24?
How does this smartStorage cold start? 
How much work load of a streaming workflow?

# 2023_0510_0016
2023_0509_2000 - 2023_0509_2150 {{{2
optimal solution:
fitness value

- task assignment strategy
    working time + distance + percentage of load + waiting_time 
- task accomplishment 

tasklist for this single aco
single aco
tasklist = [ item (weight, location, destination(1, 2), due_time) ] 
principle: order by due_time, weight, distance-to-checkout-point.

0.4*due_time, 0.4*weight, 0.2*distance-to-checkout-point.


session 
mini-batch week
a round of task accomplishment

2023_0509_2210
git branch importGA

while
    map colormap
        GA + principle = average
        SPO + principle() = average

while 
    taskList = fixed
    while 
        session: a variety of taskList.   
        each session -> list_from_GA()
    average


# 2023_0512_2153
if agent1.weight_this_trip + next_item_weight > agent1.max_load:
    back to destination
    update_state(Idle)
    agent1.reset_weight()

else:
    agent1.increase_weight(next_item_weight)
    next trip
Done

# 2023_0515_1906
Make a sequence of tasklist, in due time, or in weight, or in distance. 
Add GA Algorithm + PSO Algorithm +principle

# 2023_0519_1600
# queue is a taskList
queue = [item0, item1, item2]
agentList = [agent0, agent1, ... , agent4]
for agent in agentList:
    agent.state = 'idle'

while queue:

    # assign this item to one agent
    #for _ in range(len(agentManager.idleList)):
    while agentManager.idleList:
        if not queue:
            return

        item = queue.pop(0)
        agent = agentManager.idleList.pop(0)
        def cell_process(agent, item):
            agent.setState('busy')
            agentTakeItem(item)
            item.setState('taken')
            agent.finishTask(item)
            item.setState('completed')
            agent.setState('idle')
            agentManager.idleList.append(agent)
        cell_process(agent, item)


# 2023_05_19_18:22
1. when queue is an item, how to achieve?
2. GA Workflow, GA +principle, parameters etc. 
3. statistics for each session.