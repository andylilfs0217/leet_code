# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.maxPathSum1(root)

    def maxPathSum1(self, root: Optional[TreeNode]) -> int:

        def helper(node: Optional[TreeNode]) -> int:
            helper_ans = float('-inf')
            if not node.left and not node.right:
                helper_ans = node.val
                self.ans = max(self.ans, helper_ans)
            else:
                left = float('-inf') if not node.left else helper(node.left)
                right = float('-inf') if not node.right else helper(node.right)
                val = node.val
                helper_ans = max(val, val + left, val + right)
                self.ans = max(self.ans, helper_ans, val + left + right)
            return helper_ans

        if not root.left and not root.right:
            self.ans = root.val
        else:
            helper(root)
            pass
        return self.ans


print(Solution().maxPathSum(root=TreeNode(
    -2,
    TreeNode(1),
    None,
)))
print(Solution().maxPathSum(root=TreeNode(
    1,
    TreeNode(2),
    TreeNode(3),
)))
print(Solution().maxPathSum(root=TreeNode(
    -10,
    TreeNode(9),
    TreeNode(
        20,
        TreeNode(15),
        TreeNode(7),
    ),
)))
print(Solution().maxPathSum(root=TreeNode(
    -10,
    TreeNode(
        9,
        TreeNode(-2),
        TreeNode(11),
    ),
    TreeNode(
        20,
        TreeNode(15),
        TreeNode(7),
    ),
)))
print(Solution().maxPathSum(root=TreeNode(
    -10,
    TreeNode(9),
    TreeNode(
        20,
        TreeNode(
            15,
            TreeNode(-4),
            TreeNode(-9),
        ),
        TreeNode(7),
    ),
)))
print(Solution().maxPathSum(root=TreeNode(
    1,
    TreeNode(2),
    TreeNode(
        3,
        TreeNode(4),
        TreeNode(5),
    ),
)))