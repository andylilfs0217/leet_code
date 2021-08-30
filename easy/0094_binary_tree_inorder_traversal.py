# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursion
        # if not root:
        #     return []
        # result = []
        # result = result + self.inorderTraversal(root.left)
        # result.append(root.val)
        # result = result + self.inorderTraversal(root.right)
        # return result

        # Iteration
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if type(node) is int:
                result.append(node)
            elif node:
                stack.append(node.right)
                stack.append(node.val)
                stack.append(node.left)
        return result
