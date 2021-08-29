# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Iterative
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if type(node) is int:
                ret.append(node)
            elif node:
                stack.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret

    # Recursive
    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []
    #     result = []
    #     result = result + self.postorderTraversal(root.left)
    #     result = result + self.postorderTraversal(root.right)
    #     result.append(root.val)
    #     return result


Solution().postorderTraversal(
    TreeNode(val=1, right=TreeNode(val=2, left=TreeNode(val=3))))
