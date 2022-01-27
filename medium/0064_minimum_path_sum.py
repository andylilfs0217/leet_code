from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            if i == 0:
                dp = [0] * len(row)
            for j, cell in enumerate(row):
                if i == 0:
                    dp[j] = dp[j-1] + cell if j != 0 else cell
                else:
                    dp[j] = min(dp[j], dp[j-1]) + \
                        cell if j != 0 else dp[j] + cell
        return dp[-1]


Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
