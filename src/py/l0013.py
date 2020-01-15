class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        slist = list(s)
        slist.reverse()
        valueDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        value = 0
        i = 0
        while i < len(slist):
            if i + 1 < len(slist) and (\
                (slist[i] in ("V", "X") and slist[i + 1] == "I") or\
                (slist[i] in ("L", "C") and slist[i + 1] == "X") or\
                (slist[i] in ("D", "M") and slist[i + 1] == "C")):
                value += (valueDict[slist[i]] - valueDict[slist[i + 1]])
                i += 2
            else:
                value += valueDict[slist[i]]
                i += 1
        return value

if __name__ == "__main__":
    s = Solution()
    romanStrs = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
    for c in romanStrs:
        print(c, s.romanToInt(c))

                
