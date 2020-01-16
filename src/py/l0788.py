class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        B = None
        #             0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        rotateDict = ["0", "1", "5", B, B, "2", "9", B, "8", "6"]
        goodSet = set(["0", "1", "2", "5", "6", "8", "9"]) 
        cnt = 0
        for i in range(1, N+1):
            bitList = list(str(i))
            #print(set(bitList) - goodSet)
            if len(set(bitList) - goodSet) == 0:
                rotatedList = [rotateDict[ord(c) - ord('0')] for c in bitList]
                if int("".join(rotatedList)) != i:
                    cnt += 1
        return cnt


if __name__ == "__main__":
    s = Solution()
    s.rotatedDigits(2)