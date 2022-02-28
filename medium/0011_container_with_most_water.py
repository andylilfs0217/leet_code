from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        max_area = 0
        while l < r:
            area = (r-l)*min(height[l], height[r])
            if area > max_area:
                max_area = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


cases = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 1]]
for case in cases:
    print(Solution().maxArea(case))
