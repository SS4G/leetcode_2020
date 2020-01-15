class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = []
        if rowIndex == 0:
            return [1,]
        if rowIndex == 1:
            return [1,1]
        for i in range(rowIndex + 1):
            nextRow = [0, ] * (i + 1)
            if i == 0:
                nextRow[0] = 1
            elif i == 1:
                nextRow[0] = 1
                nextRow[1] = 1
            else:
                nextRow[len(row)] = 1
                for i in range(len(row)):
                    if i == 0:
                        nextRow[i] = 1
                    else:
                        nextRow[i] = row[i] + row[i - 1]
            row = nextRow
        return row