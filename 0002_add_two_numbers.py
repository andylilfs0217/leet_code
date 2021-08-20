from typing import List, Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            sum = l1.val + l2.val + carry
            digit = sum % 10
            carry = sum // 10
            cur.next = ListNode(digit)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        if carry != 0:
            cur.next = ListNode(carry)
        return dummy.next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
Solution().addTwoNumbers(l1, l2)
