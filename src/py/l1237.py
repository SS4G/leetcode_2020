class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        results = []
        for x in range(1, 1001):
            yleft = 1
            yright = 1000
            while yleft <= yright:
                ymid = (yleft + yright) >> 1
                res = customfunction(x, ymid)         
                if res == z:
                    results.append([x, ymid])
                    break
                elif res < z:
                    yleft = ymid + 1
                else:
                    yright = ymid - 1
        return results