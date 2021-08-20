from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        MIN_STR_LEN = min(map(len, strs))

Solution().longestCommonPrefix(strs=["flower","flow","flight"])