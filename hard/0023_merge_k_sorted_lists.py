# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self,
                    lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.mergeKLists1(lists)

    def mergeKLists1(self,
                     lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode()
        num_list = []
        for l in lists:
            while l:
                heapq.heappush(num_list, l.val)
                l = l.next
        temp = ans
        while num_list:
            num = heapq.heappop(num_list)
            temp.next = ListNode(num)
            temp = temp.next
        ans = ans.next
        return ans


Solution().mergeKLists(lists=[
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
])
Solution().mergeKLists(lists=[])
Solution().mergeKLists(lists=[[]])
