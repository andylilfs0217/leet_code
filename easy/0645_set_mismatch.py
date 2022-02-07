import enum
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        exist = [0] * len(nums)
        for num in nums:
            exist[num-1] += 1
        for i, num in enumerate(exist):
            if num == 0:
                miss = i + 1
            elif num == 2:
                dup = i + 1
        return [dup, miss]
