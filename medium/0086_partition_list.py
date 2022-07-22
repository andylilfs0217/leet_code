# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        return self.partition1(head, x)

    # Two pointer. Time: O(n), Space: O(1)
    def partition1(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp_head = ListNode(0, head)
        smaller_pointer, bigger_pointer = temp_head, temp_head
        isStart = True
        while head != None:
            if head.val < x and isStart:
                smaller_pointer = head
            elif head.val >= x:
                bigger_pointer = head
                isStart = False
            else:
                bigger_next = head.next
                smaller_next = smaller_pointer.next
                bigger_pointer.next = bigger_next
                smaller_pointer.next = head
                head.next = smaller_next
                smaller_pointer = head
            head = head.next
        return temp_head.next
