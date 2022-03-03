from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        l, r = 0, 1
        last_diff = 0
        n = len(nums)
        while r < n:
            curr_diff = nums[r] - nums[r-1]
            if curr_diff != last_diff:
                count += self.numOfArithmeticsSequence(l, r)
                l = r-1
            last_diff = curr_diff
            r += 1
        count += self.numOfArithmeticsSequence(l, r)
        return count

    def numOfArithmeticsSequence(self, l: int, r: int) -> int:
        if r-l < 3:
            return 0
        n = r-l-2
        res = (n * (n+1))//2
        return res


print(Solution().numberOfArithmeticSlices(
    [1, 2, 3, 4, 3, 2, 1, 7, 7, 7, 7, 9, 10, 5, 0]))
