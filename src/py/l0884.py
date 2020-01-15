from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        return [k for k, v in (Counter(A.split()) + Counter(B.split())).items() if v == 1]

if __name__ == "__main__":
    s = Solution()
    A = "apple apple"
    B = "banana"
    print(s.uncommonFromSentences(A, B))