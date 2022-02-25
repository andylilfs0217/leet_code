class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        i1, i2 = 0, 0
        n, m = len(v1), len(v2)
        while i1 < n or i2 < m:
            r1 = int(v1[i1]) if i1 < n else 0
            r2 = int(v2[i2]) if i2 < m else 0
            if r1 < r2:
                return -1
            elif r1 > r2:
                return 1
            i1 += 1
            i2 += 1
        return 0
