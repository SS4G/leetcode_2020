class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.modNum = 50000
        self.keyArray = [None, ] * 50000
        
    def hashfunc(self, key):
        return key % self.modNum

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
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

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashValue = self.hashfunc(key)
        if self.keyArray[hashValue] is None:
            return -1
        i = 0
        while i < len(self.keyArray[hashValue]):
            if self.keyArray[hashValue][i] is not None and self.keyArray[hashValue][i][0] == key:
                return self.keyArray[hashValue][i][1]
            i += 1
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hashValue = self.hashfunc(key)
        if self.keyArray[hashValue] is None:
            return
        i = 0
        i = 0
        while i < len(self.keyArray[hashValue]):
            if self.keyArray[hashValue][i][0] == key:
                self.keyArray[hashValue][i] = None
                return 
            i += 1
        return 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)