class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        scores = []
        for op in ops:
            if op == "+":
                scores.append(sum(scores[-2:]))
            elif op == "D":
                scores.append(2 * scores[-1])
            elif op == "C":
                scores.pop()
            else:
                scores.append(int(op))
        return sum(scores)

if __name__ == "__main__":
    l = [1, 2, 3]
    print(sum(l[-2:]))