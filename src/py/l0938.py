class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.travarseSumRange(root, L, R)

    def travarseSumRange(self, root, leftRange, rightRange):
        if root is None:
            return 0
        else:
            rootVal = root.val if leftRange <= root.val <= rightRange else 0
            
            if root.val >= leftRange:
                leftSum = self.travarseSumRange(root.left, leftRange, rightRange)
            else:
                leftSum = 0
            
            if root.val <= rightRange:
                rightSum = self.travarseSumRange(root.right, leftRange, rightRange)
            else:
                rightSum = 0

            return rootVal + leftSum + rightSum