# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node: TreeNode) -> List[int]:
            return [] if node is None else dfs(node.left) + [node.val] + dfs(node.right)

        res, i, j = [], 0, 0
        list1, list2 = dfs(root1), dfs(root2)
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1
        res += list1[i:] if j >= len(list2) else list2[j:]
        return res
