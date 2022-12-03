import collections
import heapq
from io import TextIOWrapper
import math
import statistics
from typing import List


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    res = 0
    atlas = [list(map(int, line)) for line in lines]
    DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    n, m = len(atlas), len(atlas[0])

    def checkOutOfBounds(i: int, j: int) -> bool:
        return i < 0 or j < 0 or i >= n or j >= m

    def isLowPoint(i: int, j: int) -> bool:
        return atlas[i][j] < 9

    def getBasinSize(i: int, j: int) -> int:
        res = 1
        queue = [(i, j)]
        atlas[i][j] = 9
        while queue:
            i, j = queue.pop()
            for x, y in DIRS:
                ni, nj = i + x, j + y
                if not checkOutOfBounds(ni, nj) and atlas[ni][nj] < 9:
                    atlas[ni][nj] = 9
                    res += 1
                    queue.append((ni, nj))
        return res

    basin_sizes = []
    for i in range(n):
        for j in range(m):
            if isLowPoint(i, j):
                basin_size = getBasinSize(i, j)
                basin_sizes.append(basin_size)

    basin_sizes.sort(reverse=True)
    res = math.prod(basin_sizes[:3])

    # Finish your codes here
    return res
