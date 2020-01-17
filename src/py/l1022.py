class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sumarr = [0,]
        stack = []
        self.traverseRecure(root, stack, sumarr)
        return sumarr[0]

    def traverseRecure(self, root, stack, sumarr):
        if root is None:
            return
        stack.append(root.val)
        if root.left is None and root.right is None:
            for idx, val in enumerate(stack):
                if val != 0:
                    weight = 1 << (len(stack) - 1 - idx)
                    sumarr[0] = (sumarr[0] + weight % (10**9 + 7)) % (10**9 + 7)
        else:
            self.traverseRecure(root.left, stack, sumarr)
            self.traverseRecure(root.right, stack, sumarr)
        stack.pop()
        