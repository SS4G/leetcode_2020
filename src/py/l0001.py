from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rec = defaultdict(list)
        for idx, i in enumerate(nums):
            rec[i].append(idx)
        
        for k in rec.keys():
            if 2 * k == target:
                if len(rec[k]) == 2:
                    return rec[k]
            else:
                if target - k in rec:
                    return [rec[k][0], rec[target- k][0]]
        return [-1, -1]