from typing import Annotated, List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gi, si = 0, 0
        gn, sn = len(g), len(s)
        while gi < gn and si < sn:
            if s[si] >= g[gi]:
                gi += 1
            si += 1
        return gi
