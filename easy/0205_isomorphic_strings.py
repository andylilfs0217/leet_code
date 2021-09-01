class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        toHashMap = {}
        fromHashMap = {}
        for idx, char in enumerate(s):
            if char not in toHashMap and t[idx] not in fromHashMap:
                toHashMap[char] = t[idx]
                fromHashMap[t[idx]] = char
            elif char in toHashMap and toHashMap[char] != t[idx]:
                return False
            elif t[idx] in fromHashMap and fromHashMap[t[idx]] != char:
                return False
        return True
