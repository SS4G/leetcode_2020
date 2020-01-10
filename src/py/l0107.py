class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        rows = []
        fifo = []
        rd = 0
        fifo.append((root, 1))
        rows.append([root.val,])
        while rd < len(fifo):
            node, level = fifo[rd]
            if node.left is not None:
                if len(rows) < level + 1:
                    rows.append([])
                fifo.append((node.left, level + 1))
                rows[level].append(node.left.val)

            if node.right is not None:
                if len(rows) < level + 1:
                    rows.append([])
                fifo.append((node.right, level + 1))
                rows[level].append(node.right.val)
            rd += 1
        rows.reverse()
        return rows
