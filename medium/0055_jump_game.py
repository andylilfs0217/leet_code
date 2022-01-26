from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        diff = 0
        for num in reversed(nums[:-1]):
            diff = 0 if num >= diff + 1 else diff + 1
        return diff == 0
