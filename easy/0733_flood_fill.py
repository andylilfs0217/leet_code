from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # return self.floodFill1(image, sr, sc, newColor)
        return self.floodFill2(image, sr, sc, newColor)

    # DFS
    def floodFill1(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        stack = [(sr, sc)]
        oldColor = image[sr][sc]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(image), len(image[0])
        if oldColor == newColor:
            return image
        while stack:
            cell = stack.pop()
            if image[cell[0]][cell[1]] == oldColor:
                image[cell[0]][cell[1]] = newColor
                for direction in directions:
                    new_y, new_x = cell[0]+direction[0], cell[1]+direction[1]
                    if not (new_y < 0 or new_x < 0 or new_y >= m or new_x >= n):
                        stack.append((new_y, new_x))
        return image

    # BFS
    def floodFill2(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        queue = [(sr, sc)]
        oldColor = image[sr][sc]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(image), len(image[0])
        if oldColor == newColor:
            return image
        while queue:
            cell = queue.pop(0)
            if image[cell[0]][cell[1]] == oldColor:
                image[cell[0]][cell[1]] = newColor
                for direction in directions:
                    new_y, new_x = cell[0]+direction[0], cell[1]+direction[1]
                    if not (new_y < 0 or new_x < 0 or new_y >= m or new_x >= n):
                        queue.append((new_y, new_x))
        return image


print(Solution().floodFill(
    image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2))
