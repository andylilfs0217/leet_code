# Definition for a binary tree node.
from collections import Counter
import copy
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # return self.pathSum1(root, targetSum)
        return self.pathSum2(root, targetSum)

    def pathSum1(self, root: Optional[TreeNode], targetSum: int) -> int:

        def findPaths(root: Optional[TreeNode], targetSum: int) -> int:
            ans = 0
            if not root:
                return ans
            else:
                new_targetSum = targetSum - root.val
                ans = (root.val == targetSum) + findPaths(
                    root.left, new_targetSum) + findPaths(
                        root.right, new_targetSum)
            return ans

        ans = 0
        if not root:
            return ans
        else:
            ans = findPaths(root, targetSum) + self.pathSum1(
                root.left, targetSum) + self.pathSum1(root.right, targetSum)
        return ans

    def pathSum2(self, root: Optional[TreeNode], targetSum: int) -> int:

        def helper(self, root, target, so_far, cache):
            if root:
                complement = so_far + root.val - target
                if complement in cache:
                    self.result += cache[complement]
                cache.setdefault(so_far + root.val, 0)
                cache[so_far + root.val] += 1
                self.helper(root.left, target, so_far + root.val, cache)
                self.helper(root.right, target, so_far + root.val, cache)
                cache[so_far + root.val] -= 1
            return

        ans = 0
        helper(root, targetSum, 0, {0: 1})
        return ans


# print(Solution().pathSum(
#     TreeNode(
#         10,
#         TreeNode(
#             5,
#             TreeNode(
#                 3,
#                 TreeNode(3),
#                 TreeNode(-2),
#             ),
#             TreeNode(
#                 2,
#                 None,
#                 TreeNode(1),
#             ),
#         ),
#         TreeNode(
#             -3,
#             None,
#             TreeNode(11),
#         ),
#     ), 8))

print(Solution().pathSum(
    TreeNode(
        5,
        TreeNode(
            4,
            TreeNode(
                11,
                TreeNode(7),
                TreeNode(2),
            ),
            None,
        ),
        TreeNode(
            8,
            TreeNode(
                13,
                TreeNode(5),
                TreeNode(1),
            ),
            TreeNode(
                4,
                None,
                None,
            ),
        ),
    ), 22))
