from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

#from collections import namedtuple
#NamedNode = namedtuple("NamedNode", ["node", "children_isin_stack"])
class NamedNode:
    def __init__(self, node=None, children_isin_stack=None):
        self.node = node
        self.children_isin_stack = children_isin_stack

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack = []
        result = []
        stack.append(NamedNode(node=root, children_isin_stack=False))
        while len(stack) > 0:
            if not stack[-1].children_isin_stack:
                fatherNameNode = stack[-1]
                childrenNamedNodes = [NamedNode(node=node, children_isin_stack=False) for node in reversed(stack[-1].node.children)]
                stack.extend(childrenNamedNodes)
                fatherNameNode.children_isin_stack = True
            else:
                result.append(stack.pop().node.val)
        return result
                
        