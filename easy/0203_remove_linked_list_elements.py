# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(val=-1, next=head)
        head = dummy
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
                continue
            head = head.next
        return dummy.next
