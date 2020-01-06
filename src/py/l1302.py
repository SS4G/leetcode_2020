# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            records = []
            self.travers_tree(root, 0, records)
            maxLevel = max([level for val, level in records])
            return sum([val for val, level in records if level == maxLevel])

    def travers_tree(self, root, level, node_record):
        if root is None:
            return 
        else:
            if root.left is None and root.right is None:
                node_record.append((root.val, level))
            else:
                self.travers_tree(root.left, level+1, node_record)
                self.travers_tree(root.right, level+1, node_record)
        return   
      
    