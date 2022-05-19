from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, maxSum, curMax, minSum, curMin = 0, nums[0], 0, nums[0], 0
        for a in nums:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
