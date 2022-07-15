from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # return self.maxAreaOfIsland1(grid)
        return self.maxAreaOfIsland2(grid)

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

    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        height, width = len(grid), len(grid[0])

        def bfs(i: int, j: int) -> int:
            queue = [(i, j)]
            temp_counter = 0
            for x, y in queue:
                if x >= 0 and y >= 0 and x < height and y < width:
                    cell = grid[x][y]
                    if cell == 1:
                        temp_counter += 1
                        grid[x][y] = 0
                        for di, dj in directions:
                            queue.append((x+di, y+dj))
            return temp_counter

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 0:
                    continue
                area = bfs(i, j)
                max_area = max(max_area, area)
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
