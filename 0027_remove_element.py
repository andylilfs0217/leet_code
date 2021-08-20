from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[x] = nums[i]
                x += 1
        return x
