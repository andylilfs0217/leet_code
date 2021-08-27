# Definition for a binary tree node.
from collections import deque
from typing import Collection, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def minDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     if not root.left and not root.right:
    #         return 1
    #     if not root.left:
    #         return self.minDepth(root.right) + 1
    #     if not root.right:
    #         return self.minDepth(root.left) + 1
    #     return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])

        depth = 1

        while q:
            n = len(q)

            for _ in range(n):
                node = q.popleft()

                if not node.left and not node.right:
                    return depth

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            depth += 1

        return depth
