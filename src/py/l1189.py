from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        ball = {"b": 1, "a": 1, "l":2, "o":2, "n":1}
        cnt = Counter(text)
        maxDict = {}
        for k in ball:
            if k in cnt:
                maxDict[k] = cnt[k] // ball[k]
            else:
                return 0
        #print(maxDict)
        return min(maxDict.values())

if __name__ == "__main__":
    text = "balon"
    s = Solution()
    print(s.maxNumberOfBalloons(text))