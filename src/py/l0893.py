from collections import defaultdict
class SpecialEqual:
    def __init__(self, str0):
        self.oddCharSet = defaultdict(lambda :0)
        self.evenCharSet = defaultdict(lambda :0)
        for idx, c in enumerate(str0):
            if idx & 1 == 1:
                self.oddCharSet[c] += 1
            else:
                self.evenCharSet[c] += 1
        #self.hashKey = self.getHashKey()
    
    def getHashKey(self):
        oddTuple = list(self.oddCharSet.items())
        oddTuple.sort()
        evenTuple = list(self.evenCharSet.items())
        evenTuple.sort()
        return (evenTuple, oddTuple)
        #return s

class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        keyDict = defaultdict(lambda :0)
        
        for str0 in A:
            se = SpecialEqual(str0)
            keyDict[se.hashKey] += 1
        return len(keyDict.keys())
        

if __name__ == "__main__":
    pass

