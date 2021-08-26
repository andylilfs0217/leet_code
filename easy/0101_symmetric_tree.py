# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetricTrees(left: Optional[TreeNode], right: Optional[TreeNode]):
            return (not left and not right) or (left and right and left.val == right.val and isSymmetricTrees(left.left, right.right) and isSymmetricTrees(left.right, right.left))
        return not root or isSymmetricTrees(root.left, root.right)
