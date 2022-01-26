from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_step = 0
        n = len(nums)
        dp = [0] * n
        for i, num in enumerate(nums):
            to_i = i + num
            if num != 0:
                dp[to_i] = curr_step + 1


print(Solution().jump([2, 3, 1, 1, 4]))
