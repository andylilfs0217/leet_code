class Solution:
    def myAtoi(self, s: str) -> int:
        isWithinSpaces = True
        isPositive = True
        i = 0
        isWithinNum = False
        n = len(s)
        ans = 0
        while i < n and isWithinSpaces:
            if s[i] == ' ':
                i += 1
            else:
                isWithinSpaces = False
        if i < n and s[i] == '-':
            isPositive = False
            i += 1
        elif i < n and s[i] == '+':
            i += 1
        isWithinNum = True
        while i < n and isWithinNum:
            if s[i] >= '0' and s[i] <= '9':
                ans = ans * 10 + int(s[i])
                i += 1
            else:
                isWithinNum = False
        if not isPositive:
            ans *= -1
        if ans < -(2**31):
            ans = -(2**31)
        if ans > 2**31-1:
            ans = 2**31 - 1
        return ans
