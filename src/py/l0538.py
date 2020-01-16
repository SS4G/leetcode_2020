
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        curSum = [0]
        self.traverse(root, curSum)
        return root
        
    def traverse(self, root, curSum):
        if root is None:
            return 0
        self.traverse(root.right, curSum)
        rootval = root.val
        root.val += curSum [0]
        curSum[0] += rootval
        self.traverse(root.left, curSum)