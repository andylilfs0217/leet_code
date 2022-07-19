from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # return self.numSubmatrixSumTarget1(matrix, target)
        return self.numSubmatrixSumTarget2(matrix, target)

    # Dynamic programming. Time: O((m*n)**2), Space: O(m*n)
    def numSubmatrixSumTarget1(self, matrix: List[List[int]], target: int) -> int:
        count = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = matrix[i-1][j-1] + \
                    dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        for i in range(m):
            for j in range(i+1, m+1):
                for l in range(n):
                    for r in range(l+1, n+1):
                        temp = dp[j][r] - dp[j][l] - dp[i][r] + dp[i][l]
                        if temp == target:
                            count += 1
        return count

    # Dynamic programming. Time: O((m*n)**2), Space: O(m*n)
    def numSubmatrixSumTarget2(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for x in range(m):
            for y in range(n - 1):
                matrix[x][y+1] += matrix[x][y]
        res = 0
        for y1 in range(n):
            for y2 in range(y1, n):
                preSums = {0: 1}
                s = 0
                for x in range(m):
                    s += matrix[x][y2] - (matrix[x][y1-1] if y1 > 0 else 0)
                    res += preSums.get(s - target, 0)
                    preSums[s] = preSums.get(s, 0) + 1
        return res


print(Solution().numSubmatrixSumTarget(
    matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0) == 4)
# print(Solution().numSubmatrixSumTarget(
#     matrix=[[1, -1], [-1, 1]], target=0) == 5)
# print(Solution().numSubmatrixSumTarget(
#     matrix=[[904]], target=0) == 0)
