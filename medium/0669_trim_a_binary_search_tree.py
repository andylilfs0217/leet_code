# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # self.trimBST1(root, low, high)
        self.trimBST2(root, low, high)

    # Recursive solution. Time: O(n), Space: O(n).
    def trimBST1(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return root
        elif root.val >= low and root.val <= high:
            left = self.trimBST(root.left, low, high)
            right = self.trimBST(root.right, low, high)
            root.left, root.right = left, right
            return root
        elif root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
