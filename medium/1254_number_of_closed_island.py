from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        return self.closedIsland1(grid)

    def closedIsland1(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> bool:
            if i < 0 or j < 0 or i >= n or j >= m:
                return False
            if grid[i][j] != 0:
                return True
            grid[i][j] = 2
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            is_isolated = True
            for direction in directions:
                is_isolated = dfs(
                    i+direction[0], j+direction[1]) and is_isolated
            return is_isolated

        n, m = len(grid), len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    is_isolated = dfs(i, j)
                    if is_isolated:
                        ans += 1
        return ans


print(Solution().closedIsland(
    grid=[[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
          [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
          [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
          [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
          [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]))
