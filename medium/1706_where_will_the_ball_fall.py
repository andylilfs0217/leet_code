from typing import List


class Solution:

    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = [i for i in range(n)]
        for i, row in enumerate(grid):
            next_dir = [0 for _ in range(n)]
            for j, cell in enumerate(row):
                if j + 1 < n and cell == 1 and row[j + 1] == 1:
                    # Go right
                    next_dir[j] = 1
                elif j - 1 >= 0 and cell == -1 and row[j - 1] == -1:
                    # Go left
                    next_dir[j] = -1
            for j in range(n):
                curr_pos = res[j]
                if curr_pos != -1:
                    if next_dir[curr_pos] == 0:
                        res[j] = -1
                    else:
                        res[j] += next_dir[curr_pos]
        return res


print(Solution().findBall(grid=[
    [1, 1, 1, -1, -1],
    [1, 1, 1, -1, -1],
    [-1, -1, -1, 1, 1],
    [1, 1, 1, 1, -1],
    [-1, -1, -1, -1, -1],
]))
print(Solution().findBall(grid=[[-1]]))
print(Solution().findBall(grid=[
    [1, 1, 1, 1, 1, 1],
    [-1, -1, -1, -1, -1, -1],
    [1, 1, 1, 1, 1, 1],
    [-1, -1, -1, -1, -1, -1],
]))
