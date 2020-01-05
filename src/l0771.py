class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        Jset = set(J)
        return len([1 for s in S if s in Jset])