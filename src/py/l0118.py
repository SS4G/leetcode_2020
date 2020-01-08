class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rows = []
        for i in range(numRows):
            if i == 0:
                rows.append([1,])
            elif i == 1:
                rows.append([1, 1])
            else:
                newRow = [0, ] * (i + 1)
                for j in range(i + 1):
                    if j == 0:
                        newRow[j] = 1
                    elif j == i:
                        newRow[j] = 1
                    else:
                        newRow[j] = rows[-1][j] + rows[-1][j - 1]
                rows.append(newRow)
        return rows
