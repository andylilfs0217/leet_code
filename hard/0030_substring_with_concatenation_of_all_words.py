import collections
from nis import maps
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # return self.findSubstring1(s, words)
        return self.findSubstring2(s, words)

    # Failed
    def findSubstring1(self, s: str, words: List[str]) -> List[int]:
        map1 = {}
        res = []
        s_len, words_len, word_len = len(s), len(words), len(words[0])
        for word in words:
            temp = map1
            for char in word:
                if char not in temp:
                    temp[char] = {}
                temp = temp[char]

        def checkResult(idx: int, temp_map: dict, remain_map: dict) -> bool:
            char = s[idx]
            if temp_map == {}:
                if remain_map == {}:
                    return True
                if char not in remain_map:
                    return False
                temp_map = remain_map.pop(char)
            else:
                if char not in temp_map:
                    return False
                temp_map = temp_map[char]
            idx += 1
            return checkResult(idx, temp_map, remain_map)

        for i in range(s_len - words_len*word_len):
            char = s[i]
            isSatisfy = checkResult(i, {}, dict(map1))
            if isSatisfy:
                res.append(i)
        return res

    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)

        def sliding_window(left):
            words_found = collections.defaultdict(int)
            words_used = 0
            excess_word = False

            # Do the same iteration pattern as the previous approach - iterate
            # word_length at a time, and at each iteration we focus on one word
            for right in range(left, n, word_length):
                if right + word_length > n:
                    break

                sub = s[right: right + word_length]
                if sub not in word_count:
                    # Mismatched word - reset the window
                    words_found = collections.defaultdict(int)
                    words_used = 0
                    excess_word = False
                    left = right + word_length  # Retry at the next index
                else:
                    # If we reached max window size or have an excess word
                    while right - left == substring_size or excess_word:
                        # Move the left bound over continously
                        leftmost_word = s[left: left + word_length]
                        left += word_length
                        words_found[leftmost_word] -= 1

                        if words_found[leftmost_word] == word_count[leftmost_word]:
                            # This word was the excess word
                            excess_word = False
                        else:
                            # Otherwise we actually needed it
                            words_used -= 1

                    # Keep track of how many times this word occurs in the window
                    words_found[sub] += 1
                    if words_found[sub] <= word_count[sub]:
                        words_used += 1
                    else:
                        # Found too many instances already
                        excess_word = True

                    if words_used == k and not excess_word:
                        # Found a valid substring
                        answer.append(left)

        answer = []
        for i in range(word_length):
            sliding_window(i)

        return answer


print(Solution().findSubstring(
    s="barfoothefoobarman", words=["foo", "bar"]) == [0, 9])
print(Solution().findSubstring(
    s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]) == [])
print(Solution().findSubstring(
    s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]) == [6, 9, 12])
print(Solution().findSubstring(
    s="wordgoodgoodgoodbestword", words=["word", "good", "best", "good"]) == [8])
