# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rightHead = self.reverseNodes(slow)
        while head and rightHead:
            if head.val != rightHead.val:
                return False
            head = head.next
            rightHead = rightHead.next
        return True

    def reverseNodes(self, node: ListNode) -> ListNode:
        prev = None
        while node:
            # nodeNext = node.next
            # node.next = prev
            # prev = node
            # node = nodeNext

            node.next, prev, node = prev, node, node.next
        return prev
