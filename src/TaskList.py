import numpy as np

# 随机生成货物
def generate_goods(num_goods):
    weights = np.random.randint(1, 100, num_goods)
    destinations = np.random.randint(1, 3, num_goods)
    due_times = np.random.randint(0, 24*60, num_goods)
    due_times_formatted = [f"{t // 60:02d}:{t % 60:02d}" for t in due_times]
    return list(zip(weights, destinations, due_times_formatted))

# 分配任务给机器人
def assign_tasks_to_robots(goods, robots_capacity):
    sorted_goods = sorted(goods, key=lambda x: x[2])
    tasks = [[[]] for _ in range(len(robots_capacity))]
    robot_loads = [0] * len(robots_capacity)

    while sorted_goods:
        assigned = False
        for i, capacity in enumerate(robots_capacity):
            if not sorted_goods:
                break

            weight, destination, due_time = sorted_goods[0]

            if robot_loads[i] + weight <= capacity:
                tasks[i][-1].append((weight, destination, due_time))
                robot_loads[i] += weight
                sorted_goods.pop(0)
                assigned = True
            else:
                tasks[i].append([])  # 如果超过载重量限制，为机器人创建新的任务列表
                robot_loads[i] = 0  # 重置机器人的载重量计数

    return tasks

# 示例
num_goods = 3726
goods = generate_goods(num_goods)
robots_capacity = [100, 200, 300, 400, 500]
tasks = assign_tasks_to_robots(goods, robots_capacity)

for i, robot_tasks in enumerate(tasks):
    print(f"agent{i}'s task list：")
    for j, task in enumerate(robot_tasks):
        print(f"  task list{j+1}: {task}")