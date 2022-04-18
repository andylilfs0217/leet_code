# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # return self.kthSmallest1(root, k)
        return self.kthSmallest2(root, k)

    # Recursive inorder traversal. Time: O(n), Space: O(n)
    def kthSmallest1(self, root: Optional[TreeNode], k: int) -> int:
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        return inorder(root)[k - 1]

    # Iterative inorder traversal. Time: O(H+k), Space: O(log n)
    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
