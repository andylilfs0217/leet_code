"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        prev_layer = [root] if root else []
        curr_layer = []
        while len(prev_layer) > 0 or len(curr_layer) > 0:
            while len(prev_layer) > 0:
                curr_root = prev_layer.pop(0)
                curr_root.next = prev_layer[0] if len(prev_layer) > 0 else None
                if curr_root.left:
                    curr_layer.append(curr_root.left)
                if curr_root.right:
                    curr_layer.append(curr_root.right)
            prev_layer, curr_layer = curr_layer, prev_layer
        return root
