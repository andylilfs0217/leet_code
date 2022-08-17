from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return self.lengthOfLIS1(nums)
        return self.lengthOfLIS2(nums)

    # Dynamic programming. Time: O(n^2), Space: O(n)
    def lengthOfLIS1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

    # Binary search tree. Time: O(nlogn), Space: O(n)
    def lengthOfLIS2(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                # Find the index of the smallest number >= x
                idx = bisect_left(sub, x)
                sub[idx] = x  # Replace that number with x
        return len(sub)


print(Solution().lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]) == 4)
print(Solution().lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]) == 4)
print(Solution().lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]) == 1)
