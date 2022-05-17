from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        return self.maxDistance1(grid)

    def maxDistance1(self, grid: List[List[int]]) -> int:
        def checkOutOfBound(i: int, j: int) -> bool:
            return i < 0 or j < 0 or i >= n or j >= m
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        n, m = len(grid), len(grid[0])
        queue = []
        total_land = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    total_land += 1
                    queue.append((i, j, 0))
        if total_land == 0 or total_land == n*m:
            return -1
        for a, b, d in queue:
            for x, y in directions:
                new_a, new_b = a+x, b+y
                if not checkOutOfBound(new_a, new_b) and not grid[new_a][new_b]:
                    grid[new_a][new_b] = 1
                    queue.append((new_a, new_b, d+1))
        return d
