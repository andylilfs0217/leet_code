class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        carry = 0
        num1, num2 = num1[::-1], num2[::-1]
        l1, l2 = len(num1), len(num2)
        res = [0 for _ in range(l1 + l2 + 1)]
        for i, d1 in enumerate(num1):
            carry = 0
            for j, d2 in enumerate(num2):
                digit1, digit2 = int(d1), int(d2)
                prod = digit1 * digit2 + res[i + j] + carry
                carry = prod // 10
                digit = prod % 10
                res[i + j] = digit
                pass
            res[i + j + 1] = carry
        res = res[::-1]
        for i, digit in enumerate(res):
            if digit != 0:
                break
        res = res[i:]
        res = ''.join([str(digit) for digit in res])
        return res


print(Solution().multiply(num1="2", num2="3"))
print(Solution().multiply(num1="123", num2="456"))
