from functools import reduce
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        integerset = [int(c) for c in str(abs(n))]
        return reduce(lambda x, y: x * y, integerset) - reduce(lambda x, y: x + y, integerset)