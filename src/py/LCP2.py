class Solution(object):
    def fraction(self, cont):
        """
        :type cont: List[int]
        :rtype: List[int]
        """
        numerator = 1
        denominator = cont[-1]
        i = len(cont) - 1
        while i >= 0:
            if i == len(cont) - 1:
                numerator = 1
                denominator = cont[-1]
            else:
                newNumerator = cont[i] * denominator + numerator
                numerator, denominator = denominator, newNumerator
            i -= 1
        return denominator, numerator

if __name__ == "__main__":
    s = Solution()
    cont = [3, 2, 0, 2]
    cont = [0, 0, 3]
    print(s.fraction(cont))

