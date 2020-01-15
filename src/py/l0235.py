class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        if p.val < q.val:
            smaller, greater = p.val, q.val
        else:
            smaller, greater = q.val, p.val

        stack = []
        paths = []
        self.helper(root, smaller, greater, stack, paths)
        min_length = min(len(paths[0]), len(paths[1]))
        for i in range(min_length):
            if i + 1 >= min_length or paths[0][i + 1] != paths[1][i + 1]:
                return paths[0][i]
        return None
        
    def helper(self, root, smaller, greater, stack, paths):     
        if root is None: 
            return 
        if root.val < smaller or root.val > greater:
            return
        stack.append(root)
        if root.val == smaller and root.val == greater:
            paths.append(stack[:])
            paths.append(stack[:])
        elif root.val == smaller or root.val == greater:
            paths.append(stack[:])
        self.helper(root.left, smaller, greater, stack, paths)
        self.helper(root.right, smaller, greater, stack, paths)
        stack.pop()


        
