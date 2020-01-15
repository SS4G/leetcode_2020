
class Solution(object):
    eps = 0.00001
    def calcTriangleArea(self, points):
        # xs = [x for x, y in points]
        # ys = [y for x, y in points]
        # maxX, minX = max(xs), min(xs)
        # maxY, minY = max(ys), min(ys)
        points.sort(key=lambda p: p[1])
        pX, pY, pZ = points
        #print("x={}, y={}, z={}".format(pX, pY, pZ))
        if pX[0] - pZ[0] == 0:
            #print("sd")
            return float(abs(pX[1] - pZ[1]) * abs(pX[0] - pY[0])) / 2

        k = float(pX[1] - pZ[1]) / float(pX[0] - pZ[0])
        if abs(k) < self.eps:
            return abs(pX[0] - pZ[0]) * abs(pX[1] - pY[1]) / 2.0
        b = pX[1] - k * pX[0]
        # cross point is Z2
        pY2 = [0.0, pY[1]]
        # pZ2X = 
        pY2[0] = float(pY[1] - b) / k
        area = abs(pY2[0] - pY[0]) * abs(pX[1] - pZ[1]) / 2
        return area

    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        area = 0.0
        for x in range(len(points)):
            for y in range(x + 1, len(points)):
                for z in range(y + 1, len(points)):
                    triPoints = [points[x], points[y], points[z]]
                    area = max(area, self.calcTriangleArea(triPoints))
        return area
    
if __name__ == "__main__":
    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    s = Solution()
    print(s.largestTriangleArea(points))