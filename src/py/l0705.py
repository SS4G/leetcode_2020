class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.modNum = 50000
        self.keyArray = [None, ] * 50000

    def hashfunc(self, key):
        return key % self.modNum

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        value = True
        hashValue = self.hashfunc(key)
        if self.keyArray[hashValue] is None:
            self.keyArray[hashValue] = []
        i = 0
        while i < len(self.keyArray[hashValue]):
            if self.keyArray[hashValue][i] is not None and self.keyArray[hashValue][i][0] == key:
                self.keyArray[hashValue][i] = (key, value)
                return
            i += 1
        
        i = 0
        while i < len(self.keyArray[hashValue]):
            if self.keyArray[hashValue][i] is None:
                self.keyArray[hashValue][i] = (key, value)
                return
            i += 1

        self.keyArray[hashValue].append((key, value))

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hashValue = self.hashfunc(key)
        if self.keyArray[hashValue] is None:
            return
        i = 0
        i = 0
        while i < len(self.keyArray[hashValue]):
            if self.keyArray[hashValue][i] is not None and self.keyArray[hashValue][i][0] == key:
                self.keyArray[hashValue][i] = None
                return 
            i += 1
        return 


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hashValue = self.hashfunc(key)
        if self.keyArray[hashValue] is None:
            return False
        i = 0
        while i < len(self.keyArray[hashValue]):
            if self.keyArray[hashValue][i] is not None and self.keyArray[hashValue][i][0] == key:
                return self.keyArray[hashValue][i][1]
            i += 1
        return False

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)