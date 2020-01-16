class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        size = len(arr)
        accSize = 0
        curIdx = 0
        last2ByteFlag = False # 最后的一个数字是两个字节全部写进去还是只能写进去一个
        for i in range(len(arr)): # 计算空间 看看能放下哪些数字 
            addSize = 1 if arr[i] else 2
            if accSize + addSize == size:
                curIdx = i
                last2ByteFlag = False
                break
            elif accSize + addSize > size:
                curIdx = i
                last2ByteFlag = True
                break 
            accSize += addSize
        print(last2ByteFlag, curIdx)
        wr = len(arr) - 1
        for i in range(curIdx, -1, -1): # 开始移动数字
            if i == curIdx:
                if last2ByteFlag:
                    arr[wr] = 0
                    wr -= 1
                elif not arr[i]:
                    arr[wr] = 0
                    wr -= 1
                    arr[wr] = 0
                    wr -= 1
                else:
                    arr[wr] = arr[i]
                    wr -= 1
            else:
                if arr[i]:
                    arr[wr] = arr[i]
                    wr -= 1
                else:
                    arr[wr] = 0
                    wr -= 1
                    arr[wr] = 0
                    wr -= 1

if __name__ == "__main__":
    s = Solution()
    #arr = [1,0,2,3,0,4,5,0]
    arr = [1,5,2,0,6,8,0,6,0]
    s.duplicateZeros(arr)
    print(arr)
        
        