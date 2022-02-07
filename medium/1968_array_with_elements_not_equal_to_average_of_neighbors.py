from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        ans = [-1] * n
        l, r = 0, n-1
        for i in range(n):
            if i % 2 != 0:
                ans[i] = nums[l]
                l += 1
            else:
                ans[i] = nums[r]
                r -= 1
        return ans


print(Solution().rearrangeArray([1, 2, 3, 4, 5]))
