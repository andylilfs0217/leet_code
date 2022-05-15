from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return self.maxAreaOfIsland1(grid)

    def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            if i >= 0 and j >= 0 and i < n and j < m and grid[i][j] == 1:
                area = 1
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                grid[i][j] = '#'
                for direction in directions:
                    area += dfs(i+direction[0], j+direction[1])
                return area
            else:
                return 0
        n, m = len(grid), len(grid[0])
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                area = dfs(i, j)
                max_area = max(area, max_area)
        return max_area


print(Solution().maxAreaOfIsland(grid=[
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
