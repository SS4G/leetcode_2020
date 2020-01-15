class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """  
        self.nums = nums
        self.culmitiveSum = [0, ] * len(nums)
        for idx, n in enumerate(nums):
            if idx == 0:
                self.culmitiveSum[idx] = n
            else:
                self.culmitiveSum[idx] = self.culmitiveSum[idx - 1] + n

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.culmitiveSum[j] - self.culmitiveSum[i] + self.nums[i]

