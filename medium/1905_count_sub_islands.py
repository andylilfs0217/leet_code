from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid1), len(grid1[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def checkOutOfBounds(i: int, j: int) -> bool:
            return i < 0 or j < 0 or i >= n or j >= m
        ans = 0
        for i, row in enumerate(grid2):
            for j, cell in enumerate(row):
                if cell:
                    queue = [(i, j)]
                    is_sub_island = True
                    for a, b in queue:
                        if checkOutOfBounds(a, b) or not grid2[a][b]:
                            continue
                        grid2[a][b] = 0
                        if not grid1[a][b]:
                            is_sub_island = False
                        for x, y in directions:
                            queue.append((a+x, b+y))
                    if is_sub_island:
                        ans += 1
        return ans
