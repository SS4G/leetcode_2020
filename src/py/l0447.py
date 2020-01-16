from collections import defaultdict
class Solution(object):
    def isBiao(self, I, J, K):
        return ((I[0] - J[0]) ** 2 + (I[1] - J[1]) ** 2) == ((I[0] - K[0]) ** 2 + (I[1] - K[1]) ** 2)
    
    def dist(self, I, J):
        return ((I[0] - J[0]) ** 2 + (I[1] - J[1]) ** 2)

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cnt = 0
        for i in range(len(points)): # mid
            sameEdgeCnt = defaultdict(lambda :0)
            for j in range(len(points)):
                if i != j:
                    sameEdgeCnt[self.dist(points[i], points[j])] += 1
            for dist in sameEdgeCnt:
                if sameEdgeCnt[dist] > 1:
                    cnt += (sameEdgeCnt[dist] * (sameEdgeCnt[dist] - 1))
        return cnt