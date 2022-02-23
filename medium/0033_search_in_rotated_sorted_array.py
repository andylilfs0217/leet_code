from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the smallest number first
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        new_l = l
        l, r = 0, n-1
        while l <= r:
            m = (l+r)//2
            real_m = (m+new_l) % n
            if nums[real_m] > target:
                r = m-1
            elif nums[real_m] < target:
                l = m+1
            else:
                return real_m
        return -1
