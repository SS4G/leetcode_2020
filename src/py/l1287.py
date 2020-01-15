class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) == 1:
            return arr[0]
        i = 0
        currentVal = None
        currentValCnt = 0
        while i < len(arr):
            if arr[i] != currentVal:
                currentValCnt = 1
                currentVal = arr[i]
            else:
                currentValCnt += 1
                if currentValCnt > len(arr) / 4:
                    return currentVal 
            i+=1
        return None