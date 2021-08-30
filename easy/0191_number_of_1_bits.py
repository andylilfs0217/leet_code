class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            if n == 0:
                return ans
            if n % 2 > 0:
                ans += 1
            n >>= 1
        return ans
