# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Iterative
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     ret = []
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         if node:
    #             ret.append(node.val)
    #             stack.append(node.right)
    #             stack.append(node.left)
    #     return ret

    # Recursive
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        result.append(root.val)
        result = result + self.preorderTraversal(root.left)
        result = result + self.preorderTraversal(root.right)
        return result
