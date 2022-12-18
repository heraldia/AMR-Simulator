class Strategy:

    def __init__(self, agent, item, strategy_str = None):
        self.agent = agent
        self.item = item
        if not strategy_str:
            self.algo = self.simple_hamming_distance
        elif "simple_hamming_distance" in strategy_str:
            self.algo = self.simple_hamming_distance
        elif "a_star" in strategy_str:
            self.algo = self.a_star
        elif "swam_intelligence" in strategy_str:
            self.algo = self.swam_intelligence

    def simple_hamming_distance(self):
        res = abs(self.agent.location[0] - self.item.location[0]) + abs(self.agent.location[1] - self.item.location[1]) * 2
        # times 2: because it is a round trip
        return res 

    def a_star(self):
        pass

    def get_final_path_distance(self):
        return self.algo()


"""
- metric
EA
Swam intelligence
Ant colony optimization

- idle/congestion of HumanReceiptionCounter, 
- what is the human for??
- Agent decide whether go back to HumanReceiptionCounter or reverse to take another item?
- deep learning evolution to optimize.
"""
