# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        original_head = head
        while head is not None and head.next is not None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return original_head
