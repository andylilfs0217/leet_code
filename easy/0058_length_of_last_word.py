class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0
        in_word = False
        while i >= 0:
            if s[i] == ' ' and not in_word:
                i -= 1
                continue
            elif s[i] == ' ':
                return length
            else:
                length += 1
                in_word = True
                i -= 1
        return length
