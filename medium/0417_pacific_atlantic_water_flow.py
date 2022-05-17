import collections
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # return self.pacificAtlantic1(heights)
        return self.pacificAtlantic2(heights)

    # BFS
    def pacificAtlantic2(self, matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])

        def bfs(reachable_ocean: set):
            q = collections.deque(reachable_ocean)
            while q:
                (i, j) = q.popleft()
                for (di, dj) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= di+i < m and 0 <= dj+j < n and (di+i, dj+j) not in reachable_ocean \
                            and matrix[di+i][dj+j] >= matrix[i][j]:
                        q.append((di+i, dj+j))
                        reachable_ocean.add((di+i, dj+j))
            return reachable_ocean
        pacific = set([(i, 0) for i in range(m)] + [(0, j)
                      for j in range(1, n)])
        atlantic = set([(i, n-1) for i in range(m)] + [(m-1, j)
                       for j in range(n-1)])
        return list(bfs(pacific) & bfs(atlantic))

    # DFS
    def pacificAtlantic1(self, heights: List[List[int]]) -> List[List[int]]:
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        def dfs(self, matrix, i, j, visited, m, n):
            # when dfs called, meaning its caller already verified this point
            visited[i][j] = True
            for dir in directions:
                x, y = i + dir[0], j + dir[1]
                if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                    continue
                dfs(matrix, x, y, visited, m, n)

        if not heights:
            return []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(heights)
        n = len(heights[0])
        p_visited = [[False for _ in range(n)] for _ in range(m)]

        a_visited = [[False for _ in range(n)] for _ in range(m)]
        result = []

        for i in range(m):
            # p_visited[i][0] = True
            # a_visited[i][n-1] = True
            dfs(heights, i, 0, p_visited, m, n)
            dfs(heights, i, n-1, a_visited, m, n)
        for j in range(n):
            # p_visited[0][j] = True
            # a_visited[m-1][j] = True
            dfs(heights, 0, j, p_visited, m, n)
            dfs(heights, m-1, j, a_visited, m, n)

        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i, j])
        return result
