from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter_map = Counter(nums)
        res = 0
        for k, v in counter_map.items():
            res += k if v == 1 else 0
        return res


print(Solution().sumOfUnique(nums=[1, 2, 3, 2]))
