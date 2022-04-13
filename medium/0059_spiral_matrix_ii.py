from operator import ne
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # return self.generateMatrix1(n)
        return self.generateMatrix2(n)

    # Time: O(n^2), Space: O(1) excluding the board
    # Optimized spiral traversal
    def generateMatrix1(self, n: int) -> List[List[int]]:
        def checkOutOfBounds(i, j):
            return i < 0 or j < 0 or i >= n or j >= n

        def checkVisited(i, j, board):
            return board[i][j] != 0

        direction_list = [
            (0, 1),  # Right
            (1, 0),  # Down
            (0, -1),  # Left
            (-1, 0),  # Up
        ]
        direction = 0
        cell = 1
        pos = [0, 0]
        board = [[0 for _ in range(n)] for _ in range(n)]
        while cell <= n * n:
            board[pos[0]][pos[1]] = cell
            cell += 1
            next_pos = [pos[0] + direction_list[direction]
                        [0], pos[1] + direction_list[direction][1]]
            if (checkOutOfBounds(next_pos[0], next_pos[1]) or checkVisited(next_pos[0], next_pos[1], board)):
                direction = (direction + 1) % 4
                next_pos = [pos[0] + direction_list[direction]
                            [0], pos[1] + direction_list[direction][1]]
            pos = next_pos

        return board

    # Time: O(n^2), Space: O(1) excluding the board
    # Traverse Layer by Layer in Spiral Form
    def generateMatrix2(self, n: int) -> List[List[int]]:
        board = [[0 for _ in range(n)] for _ in range(n)]
        cnt = 1
        for layer in range((n + 1) // 2):
            # direction 1 - Right
            for i in range(layer, n - layer):
                board[layer][i] = cnt
                cnt += 1
            # direction 2 - Down
            for j in range(layer + 1, n - layer):
                board[j][n - layer - 1] = cnt
                cnt += 1
            # direction 3 - Left
            for i in range(n - layer - 2, layer - 1, -1):
                board[n - layer - 1][i] = cnt
                cnt += 1
            # direction 4 - Up
            for j in range(n - layer - 2, layer, -1):
                board[j][layer] = cnt
                cnt += 1
        return board


print(Solution().generateMatrix(3))
