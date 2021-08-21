class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        def getCharNum(char: str) -> int:
            return ord(char) - 64
        num = 0
        title_len = len(columnTitle)
        for idx, char in enumerate(columnTitle):
            num += getCharNum(char) * 26**(title_len-idx-1)
        return num
