from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        return self.numMatchingSubseq1(s, words)

    def numMatchingSubseq1(self, s: str, words: List[str]) -> int:
        word_set = {}
        count = 0
        for word in words:
            temp_list = word_set.get(word[0], [])
            temp_list.append(word[1:])
            word_set[word[0]] = temp_list
        for char in s:
            expected_words = word_set.pop(char, [])
            for expected_word in expected_words:
                if expected_word == '':
                    count += 1
                else:
                    temp_list = word_set.get(expected_word[0], [])
                    temp_list.append(expected_word[1:])
                    word_set[expected_word[0]] = temp_list
        return count


print(Solution().numMatchingSubseq(
    s="abcde", words=["a", "bb", "acd", "ace"]) == 3)
print(Solution().numMatchingSubseq(s="dsahjpjauf", words=[
      "ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]) == 2)
