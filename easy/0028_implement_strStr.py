class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '' or haystack == needle:
            return 0
        idx = -1
        for i in range(0, len(haystack) - len(needle)+1):
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


Solution().strStr(haystack="abc", needle="bc")
