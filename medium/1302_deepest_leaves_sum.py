# Definition for a binary tree node.
import copy
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        return self.deepestLeavesSum1(root)

    def deepestLeavesSum1(self, root: Optional[TreeNode]) -> int:
        curr_layer = [root]
        ans = 0
        while curr_layer:
            new_layer = []
            ans = 0
            for curr_node in curr_layer:
                ans += curr_node.val
                if curr_node.left:
                    new_layer.append(curr_node.left)
                if curr_node.right:
                    new_layer.append(curr_node.right)
            curr_layer = new_layer
        return ans
