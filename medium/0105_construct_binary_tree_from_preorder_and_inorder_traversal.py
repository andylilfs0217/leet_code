# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = preorder[0]
        root_idx = inorder.index(root)
        left_inorder, right_inorder = inorder[:root_idx], inorder[root_idx+1:]
        left_subtree_num_ele = len(left_inorder)
        l, r = 1, 1+left_subtree_num_ele
        left_preorder = preorder[l:r]
        right_preorder = preorder[r:]
        left_subtree = self.buildTree(left_preorder, left_inorder)
        right_subtree = self.buildTree(right_preorder, right_inorder)
        tree = TreeNode(root, left_subtree, right_subtree)

        return tree


Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
