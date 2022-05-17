class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_idx = []
        for i, char1 in enumerate(s1):
            char2 = s2[i]
            if char1 != char2:
                diff_idx.append(i)
        if len(diff_idx) == 0:
            return True
        elif len(diff_idx) != 2:
            return False
        i1, i2 = diff_idx
        return s1[i1] == s2[i2] and s1[i2] == s2[i1]
