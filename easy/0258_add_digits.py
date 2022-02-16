class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = self.getDigitSum(num)
        return num

    def getDigitSum(self, num: int) -> int:
        ans = 0
        while num > 0:
            ans += num % 10
            num //= 10
        return ans
