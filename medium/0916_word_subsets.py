from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        return self.wordSubsets1(words1, words2)

    def wordSubsets1(self, words1: List[str], words2: List[str]) -> List[str]:
        result = []
        words2Counter = Counter()
        for word2 in words2:
            tempCounter = Counter(word2)
            for char, count in tempCounter.items():
                if count > words2Counter.get(char, 0):
                    words2Counter[char] = count
        for word1 in words1:
            isUniversal = True
            word1Counter = Counter(word1)
            for char2, count2 in words2Counter.items():
                if count2 > word1Counter.get(char2, 0):
                    isUniversal = False
                    break
            if isUniversal:
                result.append(word1)
        return result


print(Solution().wordSubsets(words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=[
      "e", "o"]) == ["facebook", "google", "leetcode"])
print(Solution().wordSubsets(words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=[
      "l", "e"]) == ["apple", "google", "leetcode"])
