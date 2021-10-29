from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        # If there is only one element in the array, the array is sorted
        if length == 1:
            return 0
        # Else
        # Loop from the beginning to find the first non-ascending element
        l = 0
        while l < length - 1 and nums[l+1] >= nums[l]:
            l += 1
        # Loop from the end to find the first non-descending element
        r = length - 1
        while r > 0 and nums[r-1] <= nums[r]:
            r -= 1
        # If left index is bigger than right index, the array is sorted
        if l > r:
            return 0
        # Else
        loc_min = min(nums[l: r+1])
        loc_max = max(nums[l: r+1])
        l = 0
        while l < length and loc_min >= nums[l]:
            l += 1
        r = length - 1
        while r >= 0 and loc_max <= nums[r]:
            r -= 1
        return r - l + 1
