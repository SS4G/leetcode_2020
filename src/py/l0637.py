from collections import defaultdict
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        level_sum = defaultdict(lambda :0)
        level_count = defaultdict(lambda :0)
        
        fifo = [(root, 0), ]
        rd = 0
        level_sum[0] += root.val
        level_count[0] += 1
        maxLevel = 0
        while rd < len(fifo):
            node, level = fifo[rd]
            if node.left is not None:
                fifo.append((node.left, level + 1))
                level_sum[level + 1] += node.left.val
                level_count[level + 1] += 1
                maxLevel = max(maxLevel, level + 1)
            if node.right is not None:
                fifo.append((node.right, level + 1))
                level_sum[level + 1] += node.right.val
                level_count[level + 1] += 1
                maxLevel = max(maxLevel, level + 1)
            rd += 1
        return [float(level_sum[i]) / level_count[i] for i in range(maxLevel + 1)]