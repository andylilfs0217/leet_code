from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def checkValidTriangle(i: int, j: int, k: int):
            return i+j > k and i+k > j and j+k > i
        nums = sorted(nums)[::-1]
        n = len(nums)
        for i in range(n-2):
            a, b, c = nums[i:i+3]
            is_valid = checkValidTriangle(a, b, c)
            if is_valid:
                return sum(nums[i:i+3])
        return 0


print(Solution().largestPerimeter([3, 2, 3, 4]))
