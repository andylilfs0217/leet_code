# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
            if length > n:
                prev = prev.next
        prev.next = prev.next.next
        ans = dummy.next
        return ans
