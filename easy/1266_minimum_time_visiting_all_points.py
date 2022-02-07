from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        curr_point = points[0]
        steps = 0
        for i in range(1, len(points)):
            point = points[i]
            diff_x, diff_y = abs(
                point[0]-curr_point[0]), abs(point[1]-curr_point[1])
            steps += max(diff_x, diff_y)
            curr_point = point
        return steps
