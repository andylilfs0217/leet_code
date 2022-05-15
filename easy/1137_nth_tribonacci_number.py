class Solution:
    def tribonacci(self, n: int) -> int:
        f = [0, 1, 1]
        if n in range(3):
            return f[n]
        for _ in range(3, n+1):
            new_f = sum(f)
            f = [f[1], f[2], new_f]
        return f[-1]
