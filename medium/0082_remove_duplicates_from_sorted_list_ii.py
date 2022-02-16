# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = ListNode(-1, head), head
        ans = prev
        is_repeating = False
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
                is_repeating = True
            elif is_repeating:
                prev.next = curr.next
                curr = curr.next
                is_repeating = False
            else:
                prev = prev.next
                curr = curr.next
        if is_repeating:
            prev.next = curr.next
        return ans.next
