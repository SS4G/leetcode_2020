class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        gain = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] >= prices[i]:
                gain += prices[i + 1] - prices[i]
        return gain