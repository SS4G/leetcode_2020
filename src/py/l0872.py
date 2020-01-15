
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leafs1 = []
        leafs2 = []
        self.helper(root1, leafs1)
        self.helper(root2, leafs2)
        return leafs1 == leafs2
    
    def helper(self, root, leafs):
        if root is None:
            return
        self.helper(root.left, leafs)
        if root.left is None and root.right is None:
            leafs.append(root.val)
        self.helper(root.right, leafs)