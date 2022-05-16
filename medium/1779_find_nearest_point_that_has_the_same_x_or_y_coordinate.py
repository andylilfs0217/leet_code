import math
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def calManhattanDistance(a: int, b: int):
            return abs(x-a) + abs(y-b) if x == a or y == b else math.inf
        ans = -1
        min_distance = math.inf
        for i, point in enumerate(points):
            distance = calManhattanDistance(point[0], point[1])
            if distance < min_distance:
                min_distance = distance
                ans = i
        return ans


print(Solution().nearestValidPoint(x=3, y=4, points=[
      [1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]))
