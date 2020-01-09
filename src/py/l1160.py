class Solution(object):
    def toIdx(self, c):
        return ord(c) - ord('a')

    def sub(self, a, b):
        return [a[i] - b[i] >= 0 for i in range(26)]
 
    def toAlphabet(self, word):
        alphabet = [0, ] * 26
        for c in word:
            alphabet[self.toIdx(c)] += 1
        return alphabet

    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        charA = self.toAlphabet(chars)
        
        res = 0
        for word in words:
            wordA = self.toAlphabet(word)
            if all(self.sub(charA, wordA)):
                res += len(word)
        return res