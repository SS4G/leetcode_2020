class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        row_cnt = 1
        currentOffset = 0
        for c in S:
            width = widths[ord(c) - ord('a')]
            if currentOffset + width > 100:
                row_cnt += 1
                currentOffset = width
            else:
                currentOffset += width
        return [row_cnt, currentOffset]
            
