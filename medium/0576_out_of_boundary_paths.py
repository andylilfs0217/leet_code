import copy
from typing import List


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # return self.findPaths1(m, n, maxMove, startRow, startColumn)
        # return self.findPaths2(m, n, maxMove, startRow, startColumn)
        return self.findPaths3(m, n, maxMove, startRow, startColumn)

    # 1. Brute force. Time: O(4^maxMove), Space: O(maxMove)
    def findPaths1(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if startRow < 0 or startRow >= m or startColumn < 0 or startColumn >= n:
            return 1
        if maxMove == 0:
            return 0
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        result = 0
        for i, j in directions:
            result += self.findPaths1(m, n, maxMove-1,
                                      startRow+i, startColumn+j)
        return result % (10**9+7)

    # 2. Memorization. Time: O(m*n*maxMove), Space: O(m*n*maxMove)
    def findPaths2(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Initialize memo
        memo = [[[-1 for _ in range(maxMove+1)]
                 for _ in range(n)] for _ in range(m)]

        def helper(m: int, n: int, maxMove: int,
                   startRow: int, startColumn: int, memo: List[List[List[int]]]):
            if startRow < 0 or startRow >= m or startColumn < 0 or startColumn >= n:
                return 1
            if maxMove == 0:
                return 0
            if memo[startRow][startColumn][maxMove] >= 0:
                return memo[startRow][startColumn][maxMove]
            memo[startRow][startColumn][maxMove] = 0
            directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
            for i, j in directions:
                memo[startRow][startColumn][maxMove] = (
                    memo[startRow][startColumn][maxMove] + helper(m, n, maxMove-1, startRow+i, startColumn+j, memo)) % (10**9 + 7)
            return memo[startRow][startColumn][maxMove]

        result = helper(m, n, maxMove, startRow, startColumn, memo)
        return result

    # Dynamic programming. Time: O(m*n*maxMove), Space: O(m*n)
    def findPaths3(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MODULO = 10**9+7
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[startRow][startColumn] = 1
        count = 0
        for _ in range(maxMove):
            temp_dp = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m - 1:
                        count = (count + dp[i][j]) % MODULO
                    if j == n - 1:
                        count = (count + dp[i][j]) % MODULO
                    if i == 0:
                        count = (count + dp[i][j]) % MODULO
                    if j == 0:
                        count = (count + dp[i][j]) % MODULO

                    if i > 0:
                        temp_dp[i][j] += dp[i-1][j]
                    if i < m-1:
                        temp_dp[i][j] += dp[i+1][j]
                    if j > 0:
                        temp_dp[i][j] += dp[i][j-1]
                    if j < n-1:
                        temp_dp[i][j] += dp[i][j+1]
            dp = copy.deepcopy(temp_dp)
        return count


print(Solution().findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))
# print(Solution().findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))
