class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        ones = []
        for i in range(32):
            if ((1 << i) & N) != 0:
                ones.append(i)
        if len(ones) <= 0:
            return 0
        maxGap = 0
        for i in range(len(ones) - 1):
            maxGap = max(maxGap, ones[i + 1] - ones[i])
        return maxGap

