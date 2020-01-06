class Solution:
    def __init__(self):
        self.moriscode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        self.morisdict = {chr(ord('a') + i): self.moriscode[i] for i in range(len(self.moriscode))}

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        translations = []
        for word in words:
            wordTranslate = []
            for c in word:
                wordTranslate.append(self.morisdict[c])
            translations.append("".join(wordTranslate))
        return len(set(translations))
