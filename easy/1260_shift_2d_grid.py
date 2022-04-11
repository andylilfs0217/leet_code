from typing import List


class Solution:
    # Time: O(m*n), Space: O(m*n)
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        vector = []
        for row in grid:
            for cell in row:
                vector.append(cell)
        k %= (m * n)
        new_vector = vector[-k:] + vector[:-k]
        new_grid = []
        for i in range(m):
            new_grid.append(new_vector[i * n: (i + 1) * n])
        return new_grid
