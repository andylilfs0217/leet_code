class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        p2, p3, p5 = 0, 0, 0
        for _ in range(1, n):
            u2, u3, u5 = 2 * dp[p2], 3 * dp[p3], 5 * dp[p5]
            umin = min(u2, u3, u5)
            if umin == u2:
                p2 += 1
            if umin == u3:
                p3 += 1
            if umin == u5:
                p5 += 1
            dp.append(umin)
        return dp[-1]


print(Solution().nthUglyNumber(10))
