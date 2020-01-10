class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rLength = len(nums)
        cLength = len(nums[0])
        newMat = None
        if rLength * cLength == r * c:
            newMat = [[0 for j in range(c)] for i in range(r)]
            for rx in range(r):
                for cx in range(c):
                    offset = rx * r + cx 
                    oldR = offset / cLength
                    oldC = offset % cLength
                    newMat[rx][cx] = nums[oldR][oldC]
        else:
            return nums
        return newMat