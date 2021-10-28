class Solution:
    # Loops
    # def isPowerOfFour(self, n: int) -> bool:
    #     while n > 1:
    #         if n % 4 != 0:
    #             return False
    #         n //= 4
    #     return n > 0

    # Recursion
    # def isPowerOfFour(self, n: int) -> bool:
    #     return n == 1 or (n > 1 and n % 4 == 0 and self.isPowerOfFour(n//4))

    # No loops/recursion solution
    def isPowerOfFour(self, num):
        return num != 0 and num & (num-1) == 0 and num & 1431655765 == num
