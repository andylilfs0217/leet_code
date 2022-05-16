from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def checkOutOfBounds(i: int, j: int) -> int:
            return i < 0 or j < 0 or i >= n or j >= m
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        ans = 0
        n, m = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    temp_ans = 0
                    queue = [(i, j)]
                    is_near_border = False
                    for a, b in queue:
                        if checkOutOfBounds(a, b):
                            is_near_border = True
                            continue
                        if grid[a][b]:
                            grid[a][b] = 0
                            temp_ans += 1
                            for x, y in directions:
                                queue.append((a+x, b+y))
                    if not is_near_border:
                        ans += temp_ans
        return ans


print(Solution().numEnclaves(grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
                             ))
