# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def addOneRow(self, root: Optional[TreeNode], val: int,
                  depth: int) -> Optional[TreeNode]:
        return self.addOneRow1(root, val, depth)

    def addOneRow1(self, root: Optional[TreeNode], val: int,
                   depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        upper_layer = [root]
        for _ in range(1, depth - 1):
            curr_layer = []
            for node in upper_layer:
                if node.left:
                    curr_layer.append(node.left)
                if node.right:
                    curr_layer.append(node.right)
            upper_layer = curr_layer
        for node in upper_layer:
            original_left_subtree, original_right_subtree = node.left, node.right
            new_left_subtree = TreeNode(val, original_left_subtree, None)
            new_right_subtree = TreeNode(val, None, original_right_subtree)
            node.left = new_left_subtree
            node.right = new_right_subtree
        return root