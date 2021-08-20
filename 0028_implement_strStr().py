class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        idx = -1
        for i in (0, len(haystack) - len(needle)):
            temp_i = i
            flag = True
            for char in needle:
                if haystack[temp_i] != char:
                    flag = False
                    break
                else:
                    temp_i += 1
            if flag:
                return i
        return idx
