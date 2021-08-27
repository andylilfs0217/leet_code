from typing import List


class Solution:
    def factorial(self, n: int) -> int:
        result = 1
        for i in range(1, n):
            result *= i + 1
        return result

    def nCr(self, n: int, r: int) -> int:
        return self.factorial(n) // (self.factorial(r) * self.factorial(n-r))

    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex + 1):
            result.append(self.nCr(rowIndex, i))
        return result
