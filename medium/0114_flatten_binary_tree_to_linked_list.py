from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, __o: object) -> bool:
        return self.val == __o.val and self.left == __o.left and self.right == __o.right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # self.flatten1(root)
        self.flatten2(root)

    # Stack. Time: O(n), Space: O(n)
    def flatten1(self, root: Optional[TreeNode]) -> None:
        stack = [root]
        queue = []
        while stack:
            node = stack.pop()
            if node:
                queue.append(node)
                stack.append(node.right)
                stack.append(node.left)
        for i in range(len(queue) - 1):
            node = queue[i]
            node.left = None
            node.right = queue[i+1]

    # Time: O(n), Space: O(1)
    def flatten2(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            left = curr.left
            left_last = left
            if left:
                while left_last.right:
                    left_last = left_last.right
                left_last.right = curr.right
                curr.left = None
                curr.right = left
            curr = curr.right


# For testing
node = TreeNode(1,
                TreeNode(2,
                         TreeNode(3),
                         TreeNode(4)),
                TreeNode(5,
                         None,
                         TreeNode(6)))
expected = TreeNode(1, None, TreeNode(2, None, TreeNode(
    3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))))
Solution().flatten(node)
print(node == expected)
node = None
expected = None
Solution().flatten(node)
print(node == expected)
node = TreeNode(0)
expected = TreeNode(0)
Solution().flatten(node)
print(node == expected)
