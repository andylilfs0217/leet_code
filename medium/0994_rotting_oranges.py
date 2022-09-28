from typing import List


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        return self.orangesRotting1(grid)

    def orangesRotting1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def outOfBound(i: int, j: int) -> bool:
            return i < 0 or i >= m or j < 0 or j >= n

        ans = 0
        num_of_oranges = sum(sum([cell > 0 for cell in row]) for row in grid)
        num_of_rotten_oranges = sum(
            sum([cell == 2 for cell in row]) for row in grid)
        DIRECTIONS = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        )
        stack, new_stack = [], []
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell == 2:
                    stack.append((i, j))
        while stack or new_stack:
            while stack:
                i, j = stack.pop(0)
                for di, dj in DIRECTIONS:
                    ni, nj = i + di, j + dj
                    if not outOfBound(ni, nj) and grid[ni][nj] == 1:
                        num_of_rotten_oranges += 1
                        grid[ni][nj] = 2
                        new_stack.append((ni, nj))
            stack = new_stack
            new_stack = []
            if stack or new_stack:
                ans += 1
        if num_of_oranges != num_of_rotten_oranges:
            ans = -1
        return ans


print(Solution().orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(Solution().orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(Solution().orangesRotting(grid=[[0, 2]]))
