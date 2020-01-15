class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        turn1 = (1 + num_people) * num_people / 2
        turnn = lambda n: (turn1 + turn1 + num_people ** 2 * (n - 1)) * n / 2
        n = 1
        while turnn(n) <= candies:
            n += 1
        n -= 1
        results = [0, ] * num_people
        for i in range(1, num_people + 1):
            results[i - 1] += (i + i + num_people * (n - 1)) * n / 2
        print(results)
        restCandies = candies - sum(results)
        i = 0
        base = 1 + n * num_people 
        while restCandies > 0:
            lastAllocate = base + i
            results[i] += min(lastAllocate, restCandies)
            restCandies -= lastAllocate
            i += 1
        return results

if __name__ == "__main__":
    candies = 10
    num_people = 3
    s = Solution()
    result = s.distributeCandies(candies, num_people)
    print(result)



