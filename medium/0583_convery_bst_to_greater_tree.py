# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum = 0
    stack = []

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # res = self.convertBST1(root)
        res = self.convertBST2(root)
        return res

    # Time: O(n), Space: O(n), recursion
    def convertBST1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.convertBST1(root.right)
        root.val += self.sum
        self.sum = root.val
        self.convertBST1(root.left)
        return root

    # Time: O(n), Space: O(n), iteration
    def convertBST2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        node = root
        stack = []
        while stack or node is not None:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            # all nodes with values between the current and its parent lie in
            # the left subtree.
            node = node.left

        return root


root = TreeNode(4,
                TreeNode(1,
                         TreeNode(0),
                         TreeNode(2,
                                  TreeNode(3))),
                TreeNode(6,
                         TreeNode(5),
                         TreeNode(7,
                                  right=TreeNode(8))))
print(Solution().convertBST(root))
