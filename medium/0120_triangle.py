from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        MAX = 10**4 + 1
        dp = [0] * len(triangle)
        dp[0] = triangle[0][0]
        for row_idx in range(1, len(triangle)):
            row_len = len(triangle[row_idx])
            prev_dp = dp.copy()
            for i, num in enumerate(triangle[row_idx]):
                left = MAX if i-1 < 0 else prev_dp[i-1]
                right = MAX if i+1 >= row_len else prev_dp[i]
                dp[i] = min(left, right) + num
        return min(dp)
