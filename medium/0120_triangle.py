from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        def getMin(left: int, right: int) -> int:
            if left and right:
                return min(left, right)
            elif left:
                return left
            elif right:
                return right
            else:
                return 0

        tri_len = len(triangle)
        last_dp = [0] * tri_len
        dp = [0] * tri_len
        for row in triangle:
            row_len = len(row)
            last_dp = dp.copy()
            for i, cell in enumerate(row):
                up_left = None if i == 0 else last_dp[i-1]
                up_right = None if i == row_len - 1 else last_dp[i]
                dp[i] = getMin(up_left, up_right) + cell
        return min(dp)


Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
