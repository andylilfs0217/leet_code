class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ''
        while i >= 0 or j >= 0:
            a_digit = 0 if i < 0 else a[i]
            b_digit = 0 if j < 0 else b[j]
            digit = (int(a_digit) + int(b_digit) + carry) % 2
            carry = (int(a_digit) + int(b_digit) + carry) // 2
            result = str(digit) + result
            i -= 1
            j -= 1
        if carry != 0:
            result = str(carry) + result
        return result


Solution().addBinary(a="11", b="1")
