# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def treeToList(node: Optional[TreeNode]):
            if not node:
                return []
            return treeToList(node.left) + [node.val] + treeToList(node.right)

        asc_list = treeToList(root)
        diff_list = []
        for i in range(1, len(asc_list)):
            diff_list.append(asc_list[i] - asc_list[i-1])
        return min(diff_list)
