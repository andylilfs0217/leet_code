from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # return self.findAnagrams1(s, p)
        return self.findAnagrams2(s, p)

    # O(nm) time, O(1) space
    def findAnagrams1(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        p_counter = Counter(p)
        res = []
        for l in range(0, n-m+1):
            r = l+m
            window_counter = Counter(s[l:r])
            if p_counter == window_counter:
                res.append(l)
        return res


cases = [["cbaebabacd", "abc"], ["abab", "ab"]]
for case in cases:
    print(Solution().findAnagrams(case[0], case[1]))
