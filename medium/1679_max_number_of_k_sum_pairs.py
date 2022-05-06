from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter_map = Counter(nums)
        total = 0
        while counter_map:
            num1, count1 = counter_map.popitem()
            num2 = k - num1
            if num1 == num2:
                total += count1//2
            else:
                count2 = counter_map.pop(num2, 0)
                total += min(count1, count2)
        return total


print(Solution().maxOperations([1, 2, 3, 4, 5], 3))
