class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmpVal = 0
        maxVal = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tmpVal += 1
            else:
                maxVal = max(tmpVal, maxVal)
                tmpVal = 0
        maxVal = max(tmpVal, maxVal)
        return maxVal
        