from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid_i = (r+l)//2
            mid = nums[mid_i]
            if mid < target:
                l = mid_i + 1
            elif mid > target:
                r = mid_i - 1
            else:
                l = r = mid_i
                break
        if l > r:
            l = r = -1
        else:
            while l > 0 and nums[l-1] == target:
                l -= 1
            while r < n-1 and nums[r+1] == target:
                r += 1
        return [l, r]
