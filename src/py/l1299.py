from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currentMaxVal = -1
        maxValArr = [None,] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                maxValArr[i] = -1
                currentMaxVal = arr[i]
            else:
                maxValArr[i] = currentMaxVal
                currentMaxVal = max((currentMaxVal, arr[i]))
        return maxValArr

if __name__ == "__main__":
    s = Solution()
    arr = [17,18,5,4,6,1]
    print(s.replaceElements(arr))