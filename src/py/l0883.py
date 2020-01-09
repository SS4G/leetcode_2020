class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rowLength = len(grid)
        colLength = len(grid[0])
        fromTop = 0
        for r in range(rowLength):
            for c in range(colLength):
                if grid[r][c] != 0:
                    fromTop += 1
        
        fromLeft = 0
        for r in range(rowLength):
            fromLeft += max(grid[r])
        
        fromFront = 0
        for c in range(colLength):
            fromFront += max([grid[r][c] for r in range(rowLength)])
        return fromTop + fromFront + fromLeft
        


