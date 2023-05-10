class GA(object):

    """
    Genetic Algorithm
    """

    def __init__(self, originalItemList=None):
        if not originalItemList:
            self._list = []
        else:
            self._list = originalItemList

    def generate(self, originalItemList):
        self._list = originalItemList
        return self._list
        
