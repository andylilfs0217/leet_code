from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def robInList(nums: List[int]) -> int:
            len_nums = len(nums)
            if len_nums == 0:
                return 0
            prev1, prev2 = 0, 0
            for num in nums:
                curr = max(prev1 + num, prev2)
                prev1, prev2 = prev2, curr
            return prev2

        return max(nums[0] + robInList(nums[2:-1]), robInList(nums[1:]))
