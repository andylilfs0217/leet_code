class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1]
        if n == 0 or n == 1:
            return f[n]
        for _ in range(2, n+1):
            new_f = sum(f)
            f[0], f[1] = f[1], new_f
        return f[-1]
