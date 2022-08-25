from collections import Counter
import collections
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return self.longestConsecutive1(nums)
        return self.longestConsecutive2(nums)

    # Failed
    def longestConsecutive1(self, nums: List[int]) -> int:
        consecutiveCounter = {}
        for num in nums:
            if consecutiveCounter.get(num, -1) == -1:
                consecutiveCounter[num] = 0
        res = 0
        for num, count in consecutiveCounter.items():
            if count > 0:
                continue

            stack = [num]
            currNum = num + 1
            currRes = 0
            while currNum in consecutiveCounter:
                currCount = consecutiveCounter[currNum]
                if currCount == 0:
                    stack.append(currNum)
                else:
                    currRes = currCount
                currNum += 1
            while stack:
                currNum = stack.pop()
                currRes += 1
                consecutiveCounter[currNum] = currRes
            res = max(res, currRes)

        return res

    def longestConsecutive2(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


print(Solution().longestConsecutive(nums=[100, 4, 200, 1, 3, 2]) == 4)
print(Solution().longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9)
