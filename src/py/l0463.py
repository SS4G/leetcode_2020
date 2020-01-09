class Solution(object):
    def calcCnt(self, grid, r, c, rL, cL):
        cnt = 0
        if r == 0:
            cnt += 1
        elif grid[r - 1][c] == 0:
            cnt += 1

        if r == rL - 1:
            cnt += 1
        elif grid[r + 1][c] == 0:
            cnt += 1
        
        if c == 0:
            cnt += 1
        elif grid[r][c - 1] == 0:
            cnt += 1
            
        if c == cL - 1:
            cnt += 1
        elif grid[r][c + 1] == 0:
            cnt += 1
        
        return cnt

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rLength = len(grid)
        cLength = len(grid[0])
        totalCnt = 0
        for rx in range(rLength):
            for cx in range(cLength):
                if grid[rx][cx] == 0:
                    continue
                else:
                    totalCnt += self.calcCnt(grid, rx, cx, rLength, cLength)
        return totalCnt