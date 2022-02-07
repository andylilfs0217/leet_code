from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_total = sum(nums[0:k])
        total = max_total
        i, j = 1, k
        while j < len(nums):
            total += nums[j] - nums[i-1]
            max_total = max(total, max_total)
            i += 1
            j += 1
        return max_total / k
