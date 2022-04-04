# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # return self.swapNodes1(head, k)
        return self.swapNodes2(head, k)

    # O(n) time and space
    def swapNodes1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node_list = []
        while not head:
            node_list.append(head.val)
            head = head.next
        node_list[k-1], node_list[-k] = node_list[-k], node_list[k-1]
        new_head = ListNode(0, None)
        curr_head = new_head
        for node in node_list:
            curr_head.next = ListNode(node, None)
            curr_head = curr_head.next
        return new_head.next

    # O(n) time and O(1) space
    def swapNodes2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Find left pointer
        l = r = head
        for _ in range(k-1):
            l = l.next
        # Find right pointer
        temp = l
        while temp.next:
            r, temp = r.next, temp.next
        # Swap
        l.val, r.val = r.val, l.val
        return head
