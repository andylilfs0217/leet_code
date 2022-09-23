class Solution:

    def concatenatedBinary(self, n: int) -> int:
        return self.concatenatedBinary1(n)

    def concatenatedBinary1(self, n: int) -> int:
        ans, M = 0, 10**9 + 7
        for x in range(1, n + 1):
            ans = (ans * (1 << (len(bin(x)) - 2)) + x) % M
        return ans


print(Solution().concatenatedBinary(1) == 1)
print(Solution().concatenatedBinary(3) == 27)
print(Solution().concatenatedBinary(12) == 505379714)