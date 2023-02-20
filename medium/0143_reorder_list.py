# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 0. Filter
        if head and head.next and head.next.next:
            # 1. Split the list into half
            first, second, t = head, head, head
            while t and t.next:
                if not t.next.next or not t.next.next.next:
                    temp = second.next
                    second.next = None
                    second = temp
                else:
                    second = second.next
                t = None if not t.next else t.next.next
            # 2. Reverse the 2nd list
            one, two, three = second, second.next, second.next.next
            one.next = None
            while two:
                two.next = one
                one = two
                two = three
                three = None if not two else two.next
            second = one
            # 3. Merge 2 lists
            while second:
                if not first.next:
                    first.next = second
                    break
                else:
                    first_temp = first.next
                    second_temp = second.next
                    first.next = second
                    second.next = first_temp
                    first = first_temp
                    second = second_temp
                pass
        pass


Solution().reorderList(ListNode(1, ListNode(2, ListNode(3))))
Solution().reorderList(ListNode(1, ListNode(2)))

Solution().reorderList(
    ListNode(
        1,
        ListNode(
            2, ListNode(3, ListNode(4, ListNode(5, ListNode(6,
                                                            ListNode(7))))))))

Solution().reorderList(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5,
                                                             ListNode(6)))))))
