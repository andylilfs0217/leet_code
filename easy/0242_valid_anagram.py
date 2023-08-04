from collections import Counter


class Solution:
    # O(mn)
    def isAnagram(self, s: str, t: str) -> bool:
        s_compared, t_compared = [False for _ in range(len(s))], [False for _ in range(len(t))]
        for char in s:
            has_same_char = False
            for i in range(len(t)):
                if t[i] == char and not t_compared[i]:
                    t_compared[i], has_same_char = True, True
                    break
            if not has_same_char:
                return False
        for char in t:
            has_same_char = False
            for i in range(len(s)):
                if s[i] == char and not s_compared[i]:
                    s_compared[i], has_same_char = True, True
                    break
            if not has_same_char:
                return False
        return True
    
    # O(m log m + n log n)
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    # O(m+n)
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter, t_counter = Counter(s), Counter(t)
        ans = True
        if s_counter != t_counter:
            ans = False
        return ans
