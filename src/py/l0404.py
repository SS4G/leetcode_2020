class Solution(object):
    def isLeaf(self, root):
        if root is None:
            return False
        return root.left is None and root.right is None

    def helper(self, root, leftSum):
        if root is None or self.isLeaf(root):
            return
        if self.isLeaf(root.left):
            leftSum[0] += root.left.val
        self.helper(root.left, leftSum)
        self.helper(root.right, leftSum)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leftSum = [0,]
        self.helper(root, leftSum)
        return leftSum[0]
        