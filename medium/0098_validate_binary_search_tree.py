# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return self.isValidBST1(root)
        return self.isValidBST2(root)

    # Failed
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        vals = []
        while stack:
            node = stack.pop()
            if node and type(node) is TreeNode:
                if node.right:
                    stack.append(node.right)
                stack.append(node.val)
                if node.left:
                    stack.append(node.left)
            elif node and type(node) is int:
                vals.append(node)
                if len(vals) > 1 and vals[-2] >= vals[-1]:
                    print(vals)
                    return False
        print(vals)
        return True

    # Success
    def isValidBST2(self, root, lessThan=float('inf'), largerThan=float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST2(root.left, min(lessThan, root.val), largerThan) and \
            self.isValidBST2(root.right, lessThan, max(root.val, largerThan))


print(Solution().isValidBST(TreeNode(2,
                                     TreeNode(1),
                                     TreeNode(3))))
print(Solution().isValidBST(TreeNode(5,
                                     TreeNode(1),
                                     TreeNode(4,
                                              TreeNode(3),
                                              TreeNode(6)))))
print(Solution().isValidBST(TreeNode(5,
                                     TreeNode(4),
                                     TreeNode(6,
                                              TreeNode(3),
                                              TreeNode(7)))))
