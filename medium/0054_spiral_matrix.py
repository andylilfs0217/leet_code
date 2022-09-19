from typing import List


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def goAround(matrix: List[List[int]], left, right, top,
                     bottom) -> List[int]:
            res = matrix[top][left:right + 1]
            for i in range(top + 1, bottom):
                res.append(matrix[i][right])
            if top != bottom:
                res += matrix[bottom][left:right + 1][::-1]
            if left != right:
                for i in range(bottom - 1, top, -1):
                    res.append(matrix[i][left])
            return res

        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1
        res = []
        while left <= right and top <= bottom:
            res += goAround(matrix, left, right, top, bottom)
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res


print(Solution().spiralOrder(matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]))
print(Solution().spiralOrder(matrix=[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]))
print(Solution().spiralOrder(matrix=[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [12, 14, 15, 16],
    [17, 18, 19, 20],
]))
print(Solution().spiralOrder(matrix=[
    [1, 2, 3, 4, 100],
    [5, 6, 7, 8, 101],
    [9, 10, 11, 12, 102],
    [13, 14, 15, 16, 103],
    [17, 18, 19, 20, 104],
    [21, 22, 23, 24, 105],
    [25, 26, 27, 28, 106],
    [29, 30, 31, 32, 107],
]))
