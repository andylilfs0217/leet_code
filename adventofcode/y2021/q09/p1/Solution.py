import collections
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
        res = True
        for x, y in DIRS:
            if not checkOutOfBounds(
                    i + x, j + y) and atlas[i + x][j + y] <= atlas[i][j]:
                res = False
        return res

    low_points = []
    for i in range(n):
        for j in range(m):
            if isLowPoint(i, j):
                low_points.append(atlas[i][j])
    risk_levels = [low_point + 1 for low_point in low_points]
    res = sum(risk_levels)

    # Finish your codes here
    return res
