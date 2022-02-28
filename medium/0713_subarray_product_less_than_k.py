from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        prod = 1
        count = 0
        for r in range(n):
            prod *= nums[r]
            while prod >= k and l <= r:
                prod //= nums[l]
                l += 1
            count += r-l+1
        return count


cases = [[[10, 5, 2, 6], 100], [[1, 2, 3], 0]]
for case in cases:
    print(Solution().numSubarrayProductLessThanK(case[0], case[1]))
