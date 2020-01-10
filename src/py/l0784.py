class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
    
    def helper(self, src, curIdx, result):
        while not src[curIdx].isalpha():
