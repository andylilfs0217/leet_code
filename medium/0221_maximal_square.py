from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_len = 0
        for i in range(len(matrix)):
            n = len(matrix[i])
            if i == 0:
                last_dp = [0] * n
                dp = [0] * n
            for j in range(n):
                dp[j] = 0 if int(matrix[i][j]) == 0 else min(
                    0 if j == 0 else dp[j-1], last_dp[j], 0 if j == 0 else last_dp[j-1]) + 1
            last_dp = dp.copy()
            max_len = max(max_len, max(dp))
        return max_len**2
