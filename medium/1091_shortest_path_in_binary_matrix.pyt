from typing import List

# TODO


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = [[0, 0]]
        length = 0
        while len(queue) > 0:
            curr = queue.pop(0)
