from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        abc = 'abcdefghijklmnopqrstuvwxyz'
        d = {}
        for count, i in enumerate(abc):
            d[i] = count
        l = len(abc)
        s = list(s)
        shifts_sum = sum(shifts)
        for i in range(len(s)):
            s[i] = abc[(d[s[i]] + shifts_sum) % l]
            shifts_sum -= shifts[i]
        return "".join(s)
