from .AgentManager import AgentManager
from .GA import GA
import sys

agentManager = AgentManager()
class TaskAssignment(object):

    """
    generated by an algorithm [tag_Genetic_Algothm]
    """

    def __init__(self, originalItemList=None, ga_object=None):
        self.itemList = originalItemList
        self.ga_object = ga_object if ga_object else GA(agentManager, self.itemList)

    def itemListGeneratedByAlgorithm(self, algorithmName, notFirstTime=0):
        """
        _summary_

        Args:
            algorithmName (_type_): _description_
            firstTime (int, optional): Defaults to 0, means this is the firstTime call; 1- not firstTime.
        """
        if not notFirstTime:
            return 
        if not algorithmName:
            pass
        if algorithmName == 'GA':
            self.itemList = self.ga_object.run(generations=100)
            total_itemList = self.ga_object.processing_total_list
            return total_itemList
        elif algorithmName == 'PSO':
            return 

    def getItemList(self):
        return self.itemList
        
