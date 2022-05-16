from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j, num in enumerate(nums):
            if j == i and num != 0:
                i += 1
            elif num != 0:
                nums[i] = num
                nums[j] = 0
                i += 1
