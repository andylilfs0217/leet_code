class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # return self.kInversePairs1(n, k)
        # return self.kInversePairs2(n, k)
        return self.kInversePairs3(n, k)

    # Memorization. Time: O(n*k*min(n,k)), Space: O(n*k)
    def kInversePairs1(self, n: int, k: int) -> int:
        MODULO = 10**9 + 7
        memo = [[-1 for _ in range(1001)] for _ in range(1001)]

        def helper(n: int, k: int) -> int:
            if n == 0:
                return 0
            if k == 0:
                return 1
            if memo[n][k] != -1:
                return memo[n][k]
            inv = 0
            for i in range(min(k, n-1) + 1):
                inv = (inv + helper(n-1, k-i)) % MODULO
            memo[n][k] = inv
            return inv
        result = helper(n, k)
        return result

    # Dynamic Programming. Time: O(n*k*min(n,k)), Space: O(n*k)
    def kInversePairs2(self, n: int, k: int) -> int:
        MODULO = 10**9+7
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(k+1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = sum(dp[i-1][j-min(j, i-1):j+1]) % MODULO
        result = dp[n][k]
        return result

    # Dynamic Programming. Time: O(n*k*min(n,k)), Space: O(n*k)
    def kInversePairs3(self, n: int, k: int) -> int:
        MODULO = 10**9 + 7
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(k+1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    temp_sum = dp[i-1][j] - dp[i-1][j-i] if j - \
                        i >= 0 else dp[i-1][j]
                    dp[i][j] = dp[i][j-1] + temp_sum
        result = dp[-1][-1] - dp[-1][-2] if k > 0 else dp[-1][-1]
        return result % MODULO


print(Solution().kInversePairs(n=3, k=0) == 1)
print(Solution().kInversePairs(n=3, k=1) == 2)
