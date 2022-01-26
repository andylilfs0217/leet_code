class Solution:
    # Dynamic programming
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(n):
                up = dp[j]
                left = 0 if j == 0 else dp[j-1]
                dp[j] = up + left
        return dp[-1]
