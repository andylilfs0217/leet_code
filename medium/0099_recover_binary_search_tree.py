# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.recoverTree1(root)

    def recoverTree1(self, root: Optional[TreeNode]) -> None:
        cur, node, cands = root, TreeNode(-float("inf")), []
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    if cur.val < node.val:
                        cands += [node, cur]
                    node = cur
                    cur = cur.right
            else:
                if cur.val < node.val:
                    cands += [node, cur]
                node = cur
                cur = cur.right

        cands[0].val, cands[-1].val = cands[-1].val, cands[0].val
