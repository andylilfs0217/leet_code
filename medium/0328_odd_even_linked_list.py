from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.oddEvenList1(head)

    def oddEvenList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Return the original list if the length == 0 or 1
        if not head or not head.next:
            return head
        odd_list, even_list = head, head.next
        first_node, second_node = head, head.next
        while second_node:
            first_node.next = second_node.next
            first_node, second_node = second_node, first_node.next
        res = odd_list
        while odd_list.next:
            odd_list = odd_list.next
        odd_list.next = even_list
        return res