from collections import Counter
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.groupAnagrams1(strs)

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


print(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]) == [
      ["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
print(Solution().groupAnagrams(strs=[""]) == [[""]])
print(Solution().groupAnagrams(strs=["a"]) == [["a"]])
