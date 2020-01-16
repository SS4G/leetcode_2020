class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        N = len(costs) >> 1
        cityA, cityB, cityAll = [], [], []
        for cost in costs:
            if cost[0] < cost[1]:
                cityA.append(cost)
            else:
                cityB.append(cost)
        cityA.sort(key=lambda r: abs(r[0] - r[1]))
        cityB.sort(key=lambda r: abs(r[0] - r[1]))
        if len(cityA) > N:
            diff = len(cityA) - N
            cityB.extend(cityA[:diff])
            cityA = cityA[diff:]
        elif len(cityB) > N:
            diff = len(cityB) - N
            cityA.extend(cityB[:diff])
            cityB = cityB[diff:]
        return sum([c[0] for c in cityA]) + sum([c[1] for c in cityB])
        
if __name__ == "__main__":
    #costs = [[10,20],[30,200],[400,50],[30,20]]
    costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    s = Solution()
    print(s.twoCitySchedCost(costs))