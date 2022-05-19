import math
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def calSlope(x0: int, y0: int, x1: int, y1: int) -> float:
            return (y1-y0)/(x1-x0) if x1-x0 != 0 else math.inf
        n = len(coordinates)
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        slope = calSlope(x0, y0, x1, y1)
        for i in range(2, n):
            x1, y1 = coordinates[i]
            if calSlope(x0, y0, x1, y1) != slope:
                return False
        return True
