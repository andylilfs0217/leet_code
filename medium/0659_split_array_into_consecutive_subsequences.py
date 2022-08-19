"""
You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).
"""

from collections import Counter
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        return self.isPossible1(nums)

    def isPossible1(self, nums: List[int]) -> bool:
        occurrence, next_num = Counter(nums), Counter()
        for num in nums:
            if occurrence.get(num, -1) == 0:
                continue
            elif next_num.get(num, -1) > 0:
                next_num[num] -= 1
                next_num[num+1] = next_num.get(num+1, 0) + 1
            elif occurrence.get(num+1, -1) > 0 and occurrence.get(num+2, -1) > 0:
                occurrence[num+1] -= 1
                occurrence[num+2] -= 1
                next_num[num+3] = next_num.get(num+3, 0) + 1
            else:
                return False
            occurrence[num] -= 1
        return True


print(Solution().isPossible(nums=[1, 2, 3, 3, 4, 5]) == True)
print(Solution().isPossible(nums=[1, 2, 3, 3, 4, 4, 5, 5]) == True)
print(Solution().isPossible(nums=[1, 2, 3, 4, 4, 5]) == False)
print(Solution().isPossible(nums=[1, 2, 3, 4, 4, 5, 5]) == False)

"""
Constraints:
- 1 <= nums.length <= 104
- -1000 <= nums[i] <= 1000
- nums is sorted in non-decreasing order.
"""
