class Solution(object):
    
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        letterDict = {}
        for idx, c in enumerate(S):
            if c.isalpha():
                letterDict[idx] = c.lower()
        bitNum = len(letterDict)
        bit2Idx = list(letterDict.keys())
        strList = list(S)
        results = []
        for i in range(2 ** bitNum):
            for j in range(bitNum):
                strIdx = bit2Idx[j]
                if (1 << j) & i != 0:
                    strList[strIdx] = strList[strIdx].lower()
                else:
                    strList[strIdx] = strList[strIdx].upper()
            results.append("".join(strList))
        return results
    

