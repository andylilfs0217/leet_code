class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a > 0 or b > 0 or c > 0:
            count += 1-max(a & 1, b & 1) if (c & 1) == 1 else (a & 1)+(b & 1)
            a, b, c = a >> 1, b >> 1, c >> 1
        return count
