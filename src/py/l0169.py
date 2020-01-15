class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        for n in nums:
            if len(stack) == 0:
                stack.append(n)
            elif stack[-1] != n:
                stack.pop()
            else:
                stack.append(n)
        return stack[0]