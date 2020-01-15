import math
class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        root = -0.5 + float((8 * candies + 1) ** 0.5) / (2 * num_people)
        downTrun = math.floor(root)
        print(root)
        turn1 = (1 + num_people) * num_people / 2
        turnn_sum = lambda n: (turn1 + turn1 + num_people**2 * (n - 1)) * n / 2
        wholeTurnCandies = turnn_sum(downTrun)
        restCandies = candies - wholeTurnCandies
        print(downTrun, wholeTurnCandies, restCandies)
        result = [0, ] * num_people
        i = 0
        while restCandies > 0:
            result[i] += (num_people * downTrun + i)
            restCandies -= result[i]
            i += 1
        for i in range(len(num_people)):
            result[i] += ((i + downTrun * num_people + i) * downTrun / 2)
        return result

if __name__ == "__main__":
    s = Solution()
    s.distributeCandies(7, 4)