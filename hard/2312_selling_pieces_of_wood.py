from typing import List


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        # return self.sellingWood1(m, n, prices)
        # return self.sellingWood2(m, n, prices)
        return self.sellingWood3(m, n, prices)

    # Brute force. Time: O(m*n*prices.length), Space: O(m*n*prices.length)
    def sellingWood1(self, m: int, n: int, prices: List[List[int]]) -> int:
        total = 0
        for h, w, price in prices:
            if h <= m and w <= n:
                temp = price + max(
                    self.sellingWood1(m-h, n, prices),
                    self.sellingWood1(m, n-w, prices))
                total = max(total, temp)
        return total

    # Memorization. Time: O(m*n*prices.length), Space: O(m*n*prices.length)
    def sellingWood2(self, m: int, n: int, prices: List[List[int]]) -> int:
        memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]

        def helper(m, n):
            if memo[m][n] != -1:
                return memo[m][n]
            total = 0
            for h, w, price in prices:
                if h <= m and w <= n:
                    temp = price + max(
                        helper(m-h, n),
                        helper(m, n-w))
                    total = max(total, temp)
            return total

        result = helper(m, n)
        return result

    # Dynamic programming. Time(m*n*(m+n) + price.length), Space: O(m*n)
    def sellingWood3(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for h, w, price in prices:
            dp[h][w] = price
        for i in range(1, m+1):
            for j in range(1, n+1):
                for ni in range(1, i//2+1):
                    dp[i][j] = max(dp[i][j], dp[ni][j] + dp[i-ni][j])
                for nj in range(1, j//2+1):
                    dp[i][j] = max(dp[i][j], dp[i][nj] + dp[i][j-nj])
        return dp[-1][-1]


print(Solution().sellingWood(m=3, n=5, prices=[
      [1, 4, 2], [2, 2, 7], [2, 1, 3]]) == 19)
print(Solution().sellingWood(m=4, n=6, prices=[
      [3, 2, 10], [1, 4, 2], [4, 1, 3]]) == 32)
