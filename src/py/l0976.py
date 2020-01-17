class Solution(object):
    def binsearch(self, array, minValue):
        """
        max index less than maxValue
        """
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = (left + right) >> 1
            if array[mid] < minValue:
                left = mid + 1
            elif array[mid] > minValue:
                right = mid - 1
            else:
                left = mid + 1
        while left < len(array) and array[left] == minValue:
            left += 1
        return left

    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        maxBoarder = 0

        for i in range(len(A) - 1, -1, -1):
            breakFlag = False
            for j in range(i - 1, -1, -1):
                gap = A[i] - A[j]
                maxLessIndex = self.binsearch(A, gap)
                if maxLessIndex >= j:
                    continue
                else:
                    #print(A[i], A[j], A[max(j - 1, maxLessIndex)])
                    maxBoarder = A[i] + A[j] + A[max(j - 1, maxLessIndex)]
                    breakFlag = True
                    break
            if breakFlag:
                break
        return maxBoarder

if __name__ == "__main__":
    s = Solution()
    A = [2, 3, 3, 4]
    s.largestPerimeter(A)
