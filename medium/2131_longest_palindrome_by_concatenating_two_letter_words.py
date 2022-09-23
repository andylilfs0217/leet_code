from collections import Counter
from typing import List


class Solution:

    def longestPalindrome(self, words: List[str]) -> int:
        return self.longestPalindrome1(words)

    def longestPalindrome1(self, words: List[str]) -> int:
        WORD_LENGTH = 2
        res = 0
        word_counter = Counter(words)
        temp = False
        for word, word_count in word_counter.items():
            reversed_word = word[::-1]
            reversed_word_count = word_counter.get(reversed_word, 0)
            is_same_word = word == reversed_word
            if is_same_word and word_count % 2:
                temp = True
                word_counter[word] -= 1
                word_count -= 1
                reversed_word_count -= 1
            max_pair = min(word_count, reversed_word_count)
            res += WORD_LENGTH * max_pair * (2 if not is_same_word else 1)
            word_counter[word] = 0
            if reversed_word in word_counter:
                word_counter[reversed_word] = 0
        res += temp * WORD_LENGTH
        return res


print(Solution().longestPalindrome(words=["lc", "cl", "gg"]) == 6)
print(Solution().longestPalindrome(
    words=["ab", "ty", "yt", "lc", "cl", "ab"]) == 8)
print(Solution().longestPalindrome(words=["cc", "ll", "xx"]) == 2)
print(Solution().longestPalindrome(
    words=["ab", "ty", "yt", "lc", "cl", "ab", "ba", "ba"]) == 16)
print(Solution().longestPalindrome(
    words=["ab", "ty", "yt", "lc", "cl", "ab", "ba", "ba", "ab"]) == 16)
print(Solution().longestPalindrome(words=[
    "ab", "ty", "yt", "lc", "cl", "ab", "ba", "ba", "ab", "gg", "gg", "gg",
    "dd", "dd"
]) == 26)
print(Solution().longestPalindrome(words=[
    "dd", "aa", "bb", "dd", "aa", "dd", "bb", "dd", "aa", "cc", "bb", "cc",
    "dd", "cc"
]) == 22)
