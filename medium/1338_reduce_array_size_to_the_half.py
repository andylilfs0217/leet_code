from collections import Counter
import heapq
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        return self.minSetSize1(arr)

    def minSetSize1(self, arr: List[int]) -> int:
        counts = Counter(arr)
        countsList = []  # (count, num)
        for num, count in counts.items():
            countsList.append((count, num))
        countsList.sort(reverse=True)
        n = len(arr)
        half = n//2
        removedCount = 0
        res = 0
        flag = True
        while flag:
            count, num = countsList.pop(0)
            removedCount += count
            res += 1
            if removedCount >= half:
                flag = False
        return res


print(Solution().minSetSize(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
print(Solution().minSetSize(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]) == 2)
print(Solution().minSetSize(arr=[7, 7, 7, 7, 7, 7]) == 1)
