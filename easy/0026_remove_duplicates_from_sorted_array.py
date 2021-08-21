from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        x = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[x] = nums[i]
                x += 1
        return x
