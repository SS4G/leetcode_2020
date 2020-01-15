class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        decodeResult = []
        while i < len(s):
            decode3 = s[i: i + 3]
            if len(decode3) == 3 and decode3[2] == "#":
                decodeResult.append(int(decode3[:2]))
                i += 3
            else:
                decodeResult.append(int(decode3[0]))
                i += 1
        #print(decodeResult)
        return "".join([chr(ord('a') + i - 1) for i in decodeResult])
