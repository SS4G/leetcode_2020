class Solution(object):

    def findNext(self, n, nums2):
        for idx, val in enumerate(nums2):
            if val == n:
                for i in range(idx + 1, len(nums2)):
                    if nums2[i] > val:
                        return nums2[i]
                return -1

    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return [self.findNext(n, nums2) for n in nums1]