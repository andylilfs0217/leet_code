# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.diameterOfBinaryTree1(root)

    def diameterOfBinaryTree1(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode]) -> List[int]:
            # Return [node_height, node_diameter]
            if not node:
                return [0, 0]
            if not node.left and not node.right:
                return [0, 0]
            if not node.left:
                right_height, right_diameter = dfs(node.right)
                return [
                    1 + right_height,
                    max(1 + right_height, right_diameter)
                ]
            if not node.right:
                left_height, left_diameter = dfs(node.left)
                return [1 + left_height, max(1 + left_height, left_diameter)]
            right_height, right_diameter = dfs(node.right)
            left_height, left_diameter = dfs(node.left)
            node_height = 1 + max(left_height, right_height)
            node_diameter = max(2 + left_height + right_height, left_diameter,
                                right_diameter)
            return [node_height, node_diameter]

        _, diameter = dfs(root)

        return diameter
