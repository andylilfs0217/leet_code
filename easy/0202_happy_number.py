class Solution:
    # O(m) space
    # def isHappy(self, n: int) -> bool:
    #     hashMap = []
    #     while n not in hashMap:
    #         hashMap.append(n)
    #         happyNum = self.calHappyNum(n)
    #         if happyNum == 1:
    #             return True
    #         n = happyNum
    #     return False

    # O(1) space
    def isHappy(self, n: int) -> bool:
        slow = self.calHappyNum(n)
        fast = self.calHappyNum(n)
        fast = self.calHappyNum(fast)
        while slow != fast:
            slow = self.calHappyNum(slow)
            fast = self.calHappyNum(fast)
            fast = self.calHappyNum(fast)
        return slow == 1

    def calHappyNum(self, n: int) -> int:
        happyNum = 0
        while n > 0:
            lastDigit = n % 10
            n //= 10
            happyNum += lastDigit ** 2
        return happyNum
