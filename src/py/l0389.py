from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """ 
        return list((Counter(t) - Counter(s)).keys())[0]

if __name__ == "__main__":
    s = Solution()
    print(s.findTheDifference("abc", "abct"))
