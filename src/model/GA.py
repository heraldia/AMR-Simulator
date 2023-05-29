from model.AgentManager import AgentManager
import random
import copy


class GA(object):
    """
    Genetic Algorithm
    """

    def __init__(self, agentManager, originalItemList=None, crossover_rate=0.7, mutation_rate=0.01):
        if not originalItemList:
            self._list = []
        else:
            self._list = originalItemList
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.agentManager = agentManager
        self.total_list = [self._list] #todo 如何在c循环下保存下来
        self.processing_total_list = copy.deepcopy(self.total_list)
        self.a = 0

    def generate(self, originalItemList):
        self._list = originalItemList
        return self._list

    def crossover(self, parent1, parent2):
        size = len(parent1)
        # Generate the crossover points
        start, end = sorted(random.sample(range(size), 2))
        # Keep the items between the crossover points from the first parent
        child1 = [-1] * size
        child2 = [-1] * size
        child1[start:end] = parent1[start:end]
        child2[start:end] = parent2[start:end]
        # Fill the remaining places with the items from the other parent in their order
        for i in range(size):
            if parent2[i] not in child1:
                for j in range(size):
                    if child1[j] == -1:
                        child1[j] = parent2[i]
                        break
            if parent1[i] not in child2:
                for j in range(size):
                    if child2[j] == -1:
                        child2[j] = parent1[i]
                        break
        return child1, child2

    def mutate(self, task_list):
        """
        Implement simple mutation
        """
        for i in range(len(task_list)):
            if random.random() < self.mutation_rate:
                # swap two tasks
                swap_index = random.randint(0, len(task_list) - 1)
                task_list[i], task_list[swap_index] = task_list[swap_index], task_list[i]
        return task_list

    def selection(self, total_list):
        """
        Implement simple selection
        """
        fitness_values = self.agentManager.fitness_results
        paired = list(zip(total_list, fitness_values))
        paired.sort(key=lambda x: x[1])
        # Select the best half (with lowest fitness values)
        selected = paired[:len(paired) // 2]
        # Extract the task lists from the pairs
        self._list = [pair[0] for pair in selected]
        return self._list

    # def fitness(self, total_list):
    #     """
    #     Implement a fitness function that favors agents with lower total busy time and distance travelled.
    #     """
    #     return self.agentManager.analyze_agents()


    def roulette_wheel_selection(self):
        pass



    def run(self, generations): #generate a set of list for calcultating fitness
        # self.total_list = [self._list]
        if self.a == 0:  #初代种群随机生成20个父辈列表
            for _ in range(20):
                parent = self._list.copy()
                random.shuffle(parent)
                self.processing_total_list.append(parent)
            self.a += 1
            return self.processing_total_list

        else:
            # for _ in range(generations):
            next_generation = []
            # 进行选择，优选出一半的个体
            self.processing_total_list = self.selection(self.processing_total_list)
            # 对每一个优选的个体进行交叉和变异
            while len(next_generation) < len(self.processing_total_list) * 2:  # 保证生成的下一代的数量和当前代的一样
                parent1 = random.choice(self.processing_total_list)
                parent2 = random.choice(self.processing_total_list)
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                next_generation.extend([child1, child2])
            self.processing_total_list = next_generation
            self.a += 1
            return self.processing_total_list
