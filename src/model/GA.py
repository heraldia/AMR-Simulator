from model.AgentManager import AgentManager
import random
import copy
import numpy as np
import collections


class GA(object):
    """
    Genetic Algorithm
    """

    def __init__(self, agentManager, originalItemList=None, crossover_rate=0.7, mutation_rate=0.1, elitism=0.1, tabu_tenure = 5):
        if not originalItemList:
            self._list = []
        else:
            self._list = originalItemList
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.agentManager = agentManager
        self.total_list = [self._list]
        self.processing_total_list = copy.deepcopy(self.total_list)
        self.tabu_list = collections.deque(maxlen=tabu_tenure)
        self.elitism = elitism
        self.a = 0

    def generate(self, originalItemList):
        self._list = originalItemList
        return self._list

    def crossover(self, parent1, parent2):
        """
            Implement Uniform Crossover
            """
        size = len(parent1)
        child1 = parent1.copy()
        child2 = parent2.copy()

        for i in range(size):
            if random.random() < self.crossover_rate:
                child1[i], child2[i] = child2[i], child1[i]  # swap genes

        return child1, child2

    # def mutate(self, task_list):
    #     # """
    #     # Implement simple mutation
    #     # """
    #     # for i in range(len(task_list)):
    #     #     if random.random() < self.mutation_rate:
    #     #         # swap two tasks
    #     #         swap_index = random.randint(0, len(task_list) - 1)
    #     #         task_list[i], task_list[swap_index] = task_list[swap_index], task_list[i]
    #     # return task_list
    #     """
    #     Implement insertion_mutation
    #     """
    #     index1 = random.randint(0, len(task_list) - 1)
    #     index2 = random.randint(0, len(task_list) - 1)
    #     task = task_list.pop(index1)
    #     task_list.insert(index2, task)
    #     return task_list
    #     # """
    #     # Implement inversion_mutation
    #     # """
    #     # index1 = random.randint(0, len(task_list) - 2)
    #     # index2 = random.randint(index1, len(task_list) - 1)
    #     # task_list[index1:index2 + 1] = reversed(task_list[index1:index2 + 1])
    #     # return task_list

    def mutate(self, task_list):
        """
        Implement tabu search in mutation
        """
        best_task_list = task_list
        best_fitness = self.agentManager.analyze_agents(task_list, record_fitness=False, record_data=False)

        # search in the neighborhood
        for _ in range(50):  # number of attempts can be a parameter
            # generate a candidate solution
            candidate_task_list = task_list.copy()
            index1 = random.randint(0, len(candidate_task_list) - 1)
            index2 = random.randint(0, len(candidate_task_list) - 1)
            candidate_task_list[index1], candidate_task_list[index2] = candidate_task_list[index2], candidate_task_list[
                index1]  # swap two tasks

            # check if it is in the tabu list
            if str(candidate_task_list) in self.tabu_list:
                continue

            # evaluate the candidate solution
            candidate_fitness = self.agentManager.analyze_agents(candidate_task_list, record_fitness=False, record_data=False)
            if candidate_fitness < best_fitness:
                best_task_list = candidate_task_list
                best_fitness = candidate_fitness

        # update the tabu list
        self.tabu_list.append(str(best_task_list))

        return best_task_list




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


    def roulette_wheel_selection(self, total_list):
        fitness_values = self.agentManager.fitness_results
        # Compute the total fitness of the population
        total_fitness = sum(fitness_values)
        # Normalize fitness values
        normalized_fitness_values = [fv / total_fitness for fv in fitness_values]
        # Calculate cumulative sum
        cumulative_sum = np.cumsum(normalized_fitness_values).tolist()

        selected = []
        for _ in range(int(len(total_list) * (1 - self.elitism))):  # Consider elitism
            random_value = random.random()
            for i, cs in enumerate(cumulative_sum):
                if random_value <= cs:
                    selected.append(total_list[i])
                    break
        return selected



    def run(self): #generate a set of list for calcultating fitness
        # self.total_list = [self._list]
        if self.a == 0:  #初代种群随机生成20个父辈列表
            for _ in range(20):
                parent = self._list.copy()
                random.shuffle(parent)
                self.processing_total_list.append(parent)
            self.a += 1
            return self.processing_total_list

        else:
            next_generation = []

            # 实现精英策略：首先保留最优秀的一部分个体
            elite_size = int(len(self.processing_total_list) * self.elitism)
            elites = self.selection(self.processing_total_list)[:elite_size]
            next_generation.extend(elites)

            # 从剩余的个体中进行轮盘赌选择
            rest_of_list = self.roulette_wheel_selection(self.processing_total_list)

            # 对选择的个体进行交叉和变异
            while len(next_generation) < len(self.processing_total_list):
                parent1 = random.choice(rest_of_list)
                parent2 = random.choice(rest_of_list)
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                next_generation.extend([child1, child2])

            self.processing_total_list = next_generation
            self.a += 1
            return self.processing_total_list
