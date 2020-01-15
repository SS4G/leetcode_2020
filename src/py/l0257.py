
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        stack = []
        paths = []
        self.traverseHelper(root, stack, paths)
        return ["->".join([str(n.val) for n in path]) for path in paths]
        
    def traverseHelper(self, root, stack, paths):
        if root is None:
            return None
        stack.append(root)
        if root.left is None and root.right is None:
            paths.append(stack[:])
        else:
            self.traverseHelper(root.left, stack, paths)
            self.traverseHelper(root.right, stack, paths)
        stack.pop()