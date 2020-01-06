class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            n = abs(nums)
            bit_cnt = 1
            while n // 10 > 0:
                n //= 10
                bit_cnt += 1
            if bit_cnt % 2 == 0:
                cnt += 1
        return cnt