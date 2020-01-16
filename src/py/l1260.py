class Solution(object):
    def shiftK(self, r, c, RL, CL, k):
        offset = r * CL + c + k
        newC = offset % CL
        newR = (offset // CL) % RL
        return newR, newC
        
        

    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        RL = len(grid)
        CL = len(grid[0])
        targetGrid = [[0 for i in range(CL)] for i in range(RL)]
        for r in range(RL):
            for c in range(CL):
                newR, newC = self.shiftK(r, c, RL, CL, k)
                targetGrid[newR][newC] = grid[r][c]
        return targetGrid

if __name__ == "__main__":
    s = Solution()
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 2
    print(s.shiftGrid(grid, k))

        
