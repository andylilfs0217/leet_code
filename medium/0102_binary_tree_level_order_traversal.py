# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.levelOrder1(root)

    def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            next_queue = []
            l = []
            for node in queue:
                l.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            ans.append(l)
            l = []
            queue = next_queue
        return ans


print(Solution().levelOrder(
    TreeNode(
        3,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7),
        ),
    )))
print(Solution().levelOrder(TreeNode(1)))
print(Solution().levelOrder(None))
