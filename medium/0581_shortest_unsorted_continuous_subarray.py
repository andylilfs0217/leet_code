from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # If there is only one element in the array, the array is sorted
        if len(nums) == 1:
            return 0
        # Else
        # Loop from the beginning to find the first non-ascending element
        l = 1
        while l < len(nums) and nums[l] > nums[l-1]:
            l += 1
        # Loop from the end to find the first non-descending element
        r = len(nums) - 2
        while r >= 0 and nums[r+1] < nums[r]:
            r -= 1
        # ? If left index is bigger than right index, the array is sorted
        if l > r:
            return 0
        # Else
        # Find the k-th minimum position that nums[l] should belong to
        i = 0
        while i < len(nums):
            if nums[l] < nums[i]:
                l = i
            i += 1
        # Find the j-th maximum position that nums[r] should belong to
        i = len(nums) - 1
        while i >= 0:
            if nums[r] > nums[i]:
                r = i
            i -= 1

        pass


print(Solution().findUnsortedSubarray([2, 6, 4, 5, 10, 9, 8, 15]))
