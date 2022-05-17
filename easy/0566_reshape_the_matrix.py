from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        if n*m != r*c:
            return mat
        curr = 0
        ans = [[1001 for _ in range(c)] for _ in range(r)]
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                a, b = curr//c, curr % c
                ans[a][b] = cell
                curr += 1
        return ans


print(Solution().matrixReshape([[1, 2], [3, 4]], 4, 1))
