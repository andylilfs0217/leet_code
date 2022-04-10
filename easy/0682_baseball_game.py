from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        total = 0
        res = []
        for op in ops:
            if op == 'C':
                total -= res.pop()
            elif op == 'D':
                res.append(res[-1] * 2)
                total += res[-1]
            elif op == '+':
                res.append(res[-1] + res[-2])
                total += res[-1]
            else:
                res.append(int(op))
                total += res[-1]
        return total
