class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = -1
        exist = {}
        repeat = set()
        for i, c in enumerate(s):
            if c in exist and c not in repeat:
                exist.pop(c)
                repeat.add(c)
            elif c not in repeat:
                exist[c] = i
        if exist:
            ans = min(exist.values())
        return ans


print(Solution().firstUniqChar("aadadaad"))
