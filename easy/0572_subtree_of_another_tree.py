# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isMatch(self, s, t):
        if not(s and t):
            return s is t
        return (s.val == t.val and
                self.isMatch(s.left, t.left) and
                self.isMatch(s.right, t.right))

    def isSubtree(self, s, t):
        if self.isMatch(s, t):
            return True
        if not s:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
