from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i, row in enumerate(obstacleGrid):
            if i == 0:
                dp = [1] * len(row)
            for j, cell in enumerate(row):
                up = 0 if i == 0 else dp[j]
                left = 0 if j == 0 else dp[j - 1]
                dp[j] = 0 if cell == 1 else 1 if i == 0 and j == 0 else up + left
        return dp[-1]
