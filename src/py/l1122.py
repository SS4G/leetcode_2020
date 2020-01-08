from collections import defaultdict, Counter
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        newArray = []
        cntDict = Counter(list(arr1))
        
        for c in arr2:
            for i in range(cntDict[c]):
                newArray.append(c)
                cntDict[c] = 0
        restArray = []
        for i in cntDict:
            if cntDict[i] != 0: 
                restArray.extend([i for j in range(cntDict[i])])
        restArray.sort()
        newArray.extend(restArray)
        return newArray

if __name__ == "__main__":
    li = [1, 1, 2, 3, 4, 5]
    c = Counter(li)
    c[2]+=1
    print(c[2])
    print(dir(c))
    for c in Counter(li).items():
        print(c)
            
            
        