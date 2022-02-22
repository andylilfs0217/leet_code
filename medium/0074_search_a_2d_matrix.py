from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # TODO
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m*n-1
        while l <= r:
            mid_i = (l+r)//2
            i, j = mid_i//m, mid_i % n
            if matrix[i][j] < target:
                l = mid_i + 1
            elif matrix[i][j] > target:
                r = mid_i - 1
            else:
                return True
        return False


print(Solution().searchMatrix(matrix=[[1, 2]], target=2))
