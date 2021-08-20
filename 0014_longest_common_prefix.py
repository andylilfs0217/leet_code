from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        MIN_STR_LEN = min(map(len, strs))
        if MIN_STR_LEN == 0:
            return ''
        common_prefix = ''
        for i in range(0, MIN_STR_LEN):
            flag = True
            char = strs[0][i]
            for str in strs:
                flag = flag and char == str[i]
            if flag:
                common_prefix += char
            if not flag or i == MIN_STR_LEN - 1:
                return common_prefix
