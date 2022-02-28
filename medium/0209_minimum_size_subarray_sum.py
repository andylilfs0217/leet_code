from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        MAX = 10**9+1
        n, l, res, total = len(nums), 0, MAX, 0
        for r in range(n):
            total += nums[r]
            exist = False
            while l <= r and total >= target:
                exist = True
                total -= nums[l]
                l += 1
            if exist:
                res = min(res, r-l+2)
        return res


cases = [
    [7, [2, 3, 1, 2, 4, 3]],
    [4, [1, 4, 4]],
    [11, [1, 1, 1, 1, 1, 1, 1, 1]]
]
for case in cases:
    print(Solution().minSubArrayLen(case[0], case[1]))
