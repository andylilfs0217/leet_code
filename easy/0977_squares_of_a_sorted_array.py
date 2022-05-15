from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # return self.sortedSquares1(nums)
        return self.sortedSquares2(nums)

    # Time: O(n log n), Space: O(1)
    def sortedSquares1(self, nums: List[int]) -> List[int]:
        return sorted([num**2 for num in nums])

    # Time: O(n), Space: O(n)
    def sortedSquares2(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        abs_nums = [abs(num) for num in nums]
        min_abs_num = min(abs_nums)
        smallest_non_neg_idx = abs_nums.index(min_abs_num)
        l, r = smallest_non_neg_idx, smallest_non_neg_idx+1
        while l >= 0 or r < n:
            if l < 0 or (r < n and abs(nums[l]) > abs(nums[r])):
                curr = nums[r]
                r += 1
            else:
                curr = nums[l]
                l -= 1
            ans.append(curr**2)
        return ans


print(Solution().sortedSquares(nums=[-1, 2, 2]))
