class Solution(object):
    def compare(self, word1, word2, charDict):
        """
        word1 < word2 = -1
        word1 > word2 = 1
        word1 == word2 = 0
        """
        for i in range(min(len(word1), len(word2))):
            if charDict[word1[i]] == charDict[word2[i]]:
                continue
            elif charDict[word1[i]] < charDict[word2[i]]:
                return -1
            else:
                return 1
        if len(word1) == len(word2):
            return 0
        elif len(word1) > len(word2):
            return 1
        else:
            return -1

    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        chardict = dict([(c, idx) for idx, c in enumerate(order)])
        for i in range(len(words) - 1):
            if self.compare(words[i], words[i + 1], chardict) > 0:
                return False
        return True
