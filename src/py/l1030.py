class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        allPointes = [(r, c) for r in range(R) for c in range(C)]
        #print(allPointes)
        allPointes.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return allPointes
            
                
if __name__ == "__main__":
    s = Solution()
    print(s.allCellsDistOrder(2, 2, 0, 0))