class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # return self.isPowerOfThree1(n)
        return self.isPowerOfThree2(n)

    def isPowerOfThree1(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            remainder = n % 3
            n //= 3
            if remainder != 0:
                return False
        return True

    def isPowerOfThree2(self, n: int) -> bool:
        return n > 0 and 3**19 % n == 0
