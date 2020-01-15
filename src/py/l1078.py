class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        words = text.split()
        rd3s = []
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                rd3s.append(words[i + 2])
        return rd3s