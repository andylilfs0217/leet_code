from typing import List


class Solution:
    # O(n)
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(0, nums[i-1])
        return max(nums)
