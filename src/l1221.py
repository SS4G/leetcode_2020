class Solution:
    def getOneBalanceSplit(self, s):
        cntDict = {'R': 0, 'L': 0}
        for idx, char in enumerate(s):
            cntDict[char] += 1
            if cntDict['R'] == cntDict['L'] and idx != len(s) - 1:
                return (s[:idx + 1], s[idx + 1:])
        return None

    def splitRecure(self, s, resultList):
        res = self.getOneBalanceSplit(s)
        if res is None:
            resultList.append(s)
        else:
            self.splitRecure(res[0], resultList)
            self.splitRecure(res[1], resultList)

    def balancedStringSplit(self, s: str) -> int:
        resultList = []
        self.splitRecure(s, resultList)
        return len(resultList)

if __name__ == "__main__":
    s = Solution()
    s0 = "LLLLRRRR"
    print(s.balancedStringSplit(s0))