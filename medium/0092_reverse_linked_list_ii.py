# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        return self.reverseBetween1(head, left, right)

    def reverseBetween1(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left - 1, right - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until right becomes 0.
        while right:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            right -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head


print(Solution().reverseBetween(head=ListNode(1, ListNode(
    2, ListNode(3, ListNode(4, ListNode(5))))), left=2, right=4) == ListNode(1, ListNode(
        4, ListNode(3, ListNode(2, ListNode(5))))))
print(Solution().reverseBetween(head=ListNode(5), left=1, right=1) == ListNode(5))
