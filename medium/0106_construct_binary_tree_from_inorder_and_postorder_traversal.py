# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, inorder: List[int],
                  postorder: List[int]) -> Optional[TreeNode]:
        return self.buildTree1(inorder, postorder)

    def buildTree1(self, inorder: List[int],
                   postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 1 and len(postorder) == 1:
            return TreeNode(inorder[0])
        if len(inorder) == 0 and len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        root_idx = inorder.index(postorder[-1])
        left_inorder, right_inorder = inorder[:root_idx], inorder[root_idx +
                                                                  1:]
        left_postorder, right_postorder = postorder[:len(
            left_inorder)], postorder[len(left_inorder):-1]
        left_tree = self.buildTree1(left_inorder, left_postorder)
        right_tree = self.buildTree1(right_inorder, right_postorder)
        root.left = left_tree
        root.right = right_tree
        return root


ans = Solution().buildTree(inorder=[9, 3, 15, 20, 7],
                           postorder=[9, 15, 7, 20, 3])
ans = Solution().buildTree(inorder=[-1], postorder=[-1])
pass
