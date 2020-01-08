class Solution(object):
    def __init__(self):
        self.primeSet = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}

    def countBits(self, x):
        cnt = 0
        for i in range(32):
            if (x & (1 << i)) != 0:
                cnt += 1
        return cnt

    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        cnt = 0
        for i in range(L, R + 1):
            if self.countBits(i) in self.primeSet:
                cnt += 1
        return cnt
        