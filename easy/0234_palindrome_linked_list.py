# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pass

    def reverseNodes(self, node: ListNode) -> ListNode:
        prev = None
        node, node.next, prev = node.next, prev, node
        return node
