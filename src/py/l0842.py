class Solution(object):
    def wordTransform(self, word, idx):
        aset = "aeiou"
        newWord = ""
        if word[0] in aset:
            newWord = word + "ma" + ("a" * idx)
        else:
            newWord = word[1:] + word[0] + "ma" + ("a" * idx)
        return newWord

    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        transformedWords = []
        for idx, word in enumerate(words):
            transformedWords.append(self.wordTransform(word, idx+1))
        return " ".join(transformedWords)