class Solution(object):

    def checkDiag(self, mat, r, c, rL, cL):
        tmpR = r 
        tmpC = c
        std = mat[r][c]
        while r < rL and c < cL:
            if mat[r][c] != std:
                return False
            r += 1
            c += 1
        return True

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rL = len(matrix)
        cL = len(matrix[0])
        for r in range(1, rL):
            if not self.checkDiag(matrix, r, 0, rL, cL):
                return False
        for c in range(0, cL):
            if not self.checkDiag(matrix, 0, c, rL, cL)
                return False
        return True
            