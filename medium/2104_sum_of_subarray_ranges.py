from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # return self.subArrayRanges1(nums)
        return self.subArrayRanges2(nums)

    # O(n^3) time
    def subArrayRanges1(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i, n):
                sub = nums[i:j+1]
                num_range = max(sub) - min(sub)
                count += num_range
        return count

    # O(n^2) time
    def subArrayRanges2(self, nums: List[int]) -> int:
        count, n = 0, len(nums)
        for i in range(n):
            curr_max, curr_min = nums[i], nums[i]
            for j in range(i+1, n):
                curr_num = nums[j]
                if curr_num > curr_max:
                    curr_max = curr_num
                if curr_num < curr_min:
                    curr_min = curr_num
                count += curr_max - curr_min
        return count

    # TODO: To understand
    # O(n) time
    def subArrayRanges3(self, nums: List[int]) -> int:
        res = 0
        inf = float('inf')
        A = [-inf] + nums + [-inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res -= A[j] * (i - j) * (j - k)
            s.append(i)

        A = [inf] + nums + [inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] < x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res
