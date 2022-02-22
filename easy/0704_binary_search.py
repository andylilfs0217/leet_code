from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid_i = (r+l)//2
            mid = nums[mid_i]
            if mid == target:
                return mid_i
            elif mid < target:
                l = mid_i + 1
            else:
                r = mid_i - 1
        return -1
