
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lastValue = [0xffffffff,]
        minDiffValue = [0xffffffff,]
        self.minDiff(root, lastValue, minDiffValue)
        return minDiffValue[0]

    def minDiff(self, root, lastValue, minDiffValue):
        if root is None:
            return
        self.minDiff(root.left, lastValue, minDiffValue)

        minDiffValue[0] = min(abs(lastValue[0] - root.val), minDiffValue[0])
        lastValue[0] = root.val
        self.minDiff(root.right, lastValue, minDiffValue)