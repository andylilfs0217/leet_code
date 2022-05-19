# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        middle = head
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
            if length % 2 == 0:
                middle = middle.next
        return middle
