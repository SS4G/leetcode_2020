from collections import Counter
class Solution(object):
    def match(self, licensePlateCnt, word):
        #print(word)
        wordCnt = Counter(word)
        #print(wordCnt, licensePlateCnt)
        for k in licensePlateCnt.keys():
            if k in wordCnt and licensePlateCnt[k] <= wordCnt[k]:
                pass
            else:
                return False
        return True

    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licensePlateCnt = Counter([c.lower() for c in licensePlate if c.isalpha()])
        words.sort(key=len)
        for word in words:
            if self.match(licensePlateCnt, word.lower()):
                return word
        return ""

if __name__ == "__main__":
    s = Solution()
    licensePlate = "1s3 PSt"
    words = ["step", "steps", "stripe", "stepple"]
    print(s.shortestCompletingWord(licensePlate, words))
    # cnt1 = Counter("Aadad")
    # cnt2 = Counter("Asa")
