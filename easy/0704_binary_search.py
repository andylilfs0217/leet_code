from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            num = nums[m]
            if num == target:
                return m
            elif num < target:
                l = m + 1
            else:
                r = m - 1
        return -1
