from model.AgentManager import AgentManager
import random


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

    def generate(self, originalItemList):
        self._list = originalItemList
        return self._list

    def crossoever(self, parent1, parent2):
        # """
        # Implement simple one-point crossover
        # """
        # crossover_index = random.randint(0, len(parent1) - 1)
        # child1 = parent1[:crossover_index] + parent2[crossover_index:]
        # child2 = parent2[:crossover_index] + parent1[crossover_index:]
        # return child1, child2
        size = len(parent1)
        # Generate the crossover points
        start, end = sorted(random.sample(range(size), 2))
        # Keep the items between the crossover points from the first parent
        child1 = [-1] * start + parent1[start:end] + [-1] * (size - end)
        child2 = [-1] * start + parent2[start:end] + [-1] * (size - end)
        # Fill the remaining places with the items from the other parent in their order
        for p in [parent2, parent1]:
            for i in range(start):
                if p[i] not in child1:
                    child1[child1.index(-1)] = p[i]
            for i in range(end, size):
                if p[i] not in child1:
                    child1[child1.index(-1)] = p[i]
        for p in [parent1, parent2]:
            for i in range(start):
                if p[i] not in child2:
                    child2[child2.index(-1)] = p[i]
            for i in range(end, size):
                if p[i] not in child2:
                    child2[child2.index(-1)] = p[i]
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
        fitness_values = self.agentManager.calculate_total_busy_time_and_distance(total_list)
        sorted_pairs = sorted(zip(total_list, fitness_values), key=lambda x: x[1])
        self._list = sorted_pairs[0][0]
        # Update total_list to only keep the best half of the items
        total_list = [pair[0] for pair in sorted_pairs[:len(sorted_pairs) // 2]]
        return total_list

    def fitness(self, total_list):
        """
        Implement a fitness function that favors agents with lower total busy time and distance travelled.
        """
        return self.agentManager.calculate_total_busy_time_and_distance(total_list)

    def run(self, generations):
        total_list = [self._list]
        for _ in range(generations):
            parent1 = self._list.copy()
            parent2 = self._list.copy()
            random.shuffle(parent1)
            random.shuffle(parent2)
            child1, child2 = self.crossoever(parent1, parent2)
            child1 = self.mutate(child1)
            child2 = self.mutate(child2)
            total_list.extend([parent1, parent2, child1, child2])
            total_list = self.selection(total_list)
        return self._list
