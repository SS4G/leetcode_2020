from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack = []
        stack.append(root)
        result = []
        while len(stack) > 0: # still hava node to be iterate
            currentNode = stack.pop()
            result.append(currentNode.val)
            revChilds = reversed(currentNode.children)
            stack.extend(revChilds)
        return result
        