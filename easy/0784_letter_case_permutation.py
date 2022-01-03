from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        if len(s) == 1:
            if s[0].isdigit():
                res.append(s[0])
            else:
                res.append(s[0].lower())
                res.append(s[0].upper())
        else:
            tail = self.letterCasePermutation(s[1:])
            if s[0].isdigit():
                res = list(map(lambda x: s[0] + x, tail))
            else:
                res = list(map(lambda x: s[0].lower() + x, tail)) + list(map(lambda x: s[0].upper() + x, tail))
        return res