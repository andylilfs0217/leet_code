import math
from typing import List


class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # return self.shortestPathBinaryMatrix1(grid)
        return self.shortestPathBinaryMatrix2(grid)

    # BFS
    def shortestPathBinaryMatrix1(self, grid: List[List[int]]) -> int:
        def checkOutOfRange(i: int, j: int, n: int) -> bool:
            return i < 0 or j < 0 or i >= n or j >= n
        directions = (
            (-1, 0),    # N
            (-1, 1),    # NE
            (0, 1),     # E
            (1, 1),     # SE
            (1, 0),     # S
            (1, -1),    # Sw
            (0, -1),    # W
            (-1, -1),   # NW
        )
        n = len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        stack = [(0, 0, 1)]  # [(i,j,prev_w)]
        grid[0][0] = 1
        for i, j, w in stack:
            if i == n-1 and j == n-1:
                return w
            for y, x in directions:
                new_i, new_j = i+y, j+x
                if not checkOutOfRange(new_i, new_j, n) and grid[new_i][new_j] == 0:
                    grid[new_i][new_j] = 1
                    stack.append((new_i, new_j, w+1))
        return -1

    # A* search
    def shortestPathBinaryMatrix2(self, grid: List[List[int]]) -> int:
        def checkOutOfRange(i: int, j: int, n: int) -> bool:
            return i < 0 or j < 0 or i >= n or j >= n
        directions = (
            (-1, 0),    # N
            (-1, 1),    # NE
            (0, 1),     # E
            (1, 1),     # SE
            (1, 0),     # S
            (1, -1),    # Sw
            (0, -1),    # W
            (-1, -1),   # NW
        )
        n = len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        pqueue = []
        return -1


print(Solution().shortestPathBinaryMatrix([
    [0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0]
]))
