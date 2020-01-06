from typing import List
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        #numSet = [False,] * (len(S) + 1)
        result = []
        inNum = 0
        deNum = len(S)
        for c in S:
            if c == 'I':
                #if len(result) == 0:
                result.append(inNum)
                inNum += 1
                #    numSet[0] = True
            else:
                result.append(deNum)
                deNum -= 1
        result.append((inNum + deNum) // 2)
        return result


