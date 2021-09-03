# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        if not root.left and not root.right:
            return [str(root.val)]
        else:
            if root.left:
                for l in self.binaryTreePaths(root.left):
                    ans.append(f"{str(root.val)}->{l}")
            if root.right:
                for l in self.binaryTreePaths(root.right):
                    ans.append(f"{str(root.val)}->{l}")
            return ans
