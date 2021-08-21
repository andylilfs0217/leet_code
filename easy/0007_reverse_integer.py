from typing import final


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31-1
        MIN_INT = -2**31

        is_neg = x < 0
        x = abs(x)
        rev = 0
        while x != 0:
            pop = x % 10
            x //= 10
            if rev > MAX_INT//10 or rev == MAX_INT//10 and pop > 7:
                return 0
            if rev < MIN_INT//10 or rev == MIN_INT//10 and pop <= -8:
                return 0
            rev = rev * 10 + pop
        if is_neg:
            rev = -rev
        return rev


print(Solution().reverse(-123))
