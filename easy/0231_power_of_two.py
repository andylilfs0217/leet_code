class Solution:
    # Bitwise operation
    # def isPowerOfTwo(self, n: int) -> bool:
    #     return n > 0 and not (n & (n-1))

    # Recursion
    # def isPowerOfTwo(self, n: int) -> bool:
    #     if n <= 0:
    #         return False
    #     if n == 1:
    #         return True
    #     if n % 2 == 0:
    #         return self.isPowerOfTwo(n // 2)
    #     return False

    # Iteration
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n % 2 != 0:
                return False
            n //= 2
        return True
