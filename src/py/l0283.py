class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        wr = 0
        rd = 0
        while rd < len(nums):
            if nums[rd] != 0:
                #flag = nums[wr] == 0
                nums[wr], nums[rd] = nums[rd], nums[wr]
                #if flag:
                #    nums[rd] = 0
                wr += 1
            rd += 1