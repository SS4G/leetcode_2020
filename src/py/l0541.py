class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        segs = []
        for i in range(0, len(s), 2*k):
            segs.append((s[i:i+k], s[i+k:i+2*k]))
        result = []
        for seg in segs:
            s0 = list(seg[0])
            s0.reverse()
            result.append("".join(s0))
            result.append(seg[1])
        return "".join(result)
        



