class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        buffer = list(S)
        leftPtr = 0
        rightPtr = len(buffer) - 1
        while leftPtr < rightPtr:
            #print(leftPtr, rightPtr)
            while 0 <= leftPtr < len(buffer) and not buffer[leftPtr].isalpha():
                leftPtr += 1
            while 0 <= rightPtr < len(buffer) and not buffer[rightPtr].isalpha():
                rightPtr -= 1
            if not 0 <= leftPtr < len(buffer) or not 0 <= rightPtr < len(buffer) or leftPtr >= rightPtr:
                break
            #print(buffer[leftPtr], buffer[rightPtr])
            buffer[leftPtr], buffer[rightPtr] = buffer[rightPtr], buffer[leftPtr]
            #print(buffer[leftPtr], buffer[rightPtr])
            leftPtr += 1
            rightPtr -= 1
        return "".join(buffer)

if __name__ == "__main__":
    s = Solution()
    str0 = "?6C40E"#"abc-18-de"
    print(s.reverseOnlyLetters(str0))