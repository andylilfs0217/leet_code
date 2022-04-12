from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # self.gameOfLife1(board)
        # self.gameOfLife2(board)
        self.gameOfLife3(board)

    # Time: O(m*n), Space: O(m*n)
    def gameOfLife1(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def getNeighbors(i: int, j: int, originalBoard: List[List[int]]) -> int:
            total = 0
            up_left = originalBoard[i-1][j-1] if i > 0 and j > 0 else 0
            up = originalBoard[i-1][j] if i > 0 else 0
            up_right = originalBoard[i-1][j+1] if i > 0 and j < n - 1 else 0
            left = originalBoard[i][j-1] if j > 0 else 0
            right = originalBoard[i][j+1] if j < n - 1 else 0
            down_left = originalBoard[i+1][j-1] if i < m - 1 and j > 0 else 0
            down = originalBoard[i+1][j] if i < m - 1 else 0
            down_right = originalBoard[i+1][j +
                                            1] if i < m - 1 and j < n - 1 else 0
            total = up_left + up + up_right + left + right + down_left + down + down_right
            return total

        def getCellStatus(cell: int, neighbors: int) -> int:
            if cell == 1 and neighbors < 2:
                return 0
            elif cell == 1 and (neighbors == 2 or neighbors == 3):
                return 1
            elif cell == 1 and neighbors > 3:
                return 0
            elif cell == 0 and neighbors == 3:
                return 1
            return cell

        m, n = len(board), len(board[0])
        originalBoard = []
        for row in board:
            originalBoard.append([])
            for cell in row:
                originalBoard[-1].append(cell)
        for i in range(m):
            for j in range(n):
                newNeighbor = getNeighbors(i, j, originalBoard)
                newCellStatus = getCellStatus(
                    originalBoard[i][j], newNeighbor)
                board[i][j] = newCellStatus

    # Time: O(m*n), Space: O(n)
    def gameOfLife2(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def getCellStatus(cell: int, neighbors: int) -> int:
            if neighbors < 2 or neighbors > 3:
                return 0
            elif neighbors == 2:
                return cell
            else:
                return 1

        def getNeighbors(i: int, j: int, last_row: List[int], curr_row: List[int]) -> int:
            total = 0
            up_left = last_row[j-1] if j > 0 else 0
            up = last_row[j]
            up_right = last_row[j+1] if j < n-1 else 0
            left = curr_row[j-1] if j > 0 else 0
            right = curr_row[j+1] if j < n-1 else 0
            down_left = board[i+1][j-1] if i < m - 1 and j > 0 else 0
            down = board[i+1][j] if i < m - 1 else 0
            down_right = board[i+1][j+1] if i < m - 1 and j < n-1 else 0
            total = up_left + up + up_right + left + right + down_left + down + down_right
            return total

        m, n = len(board), len(board[0])
        last_row = [0] * n
        curr_row = [cell for cell in board[0]]
        for i, row in enumerate(board):
            curr_row = [c for c in row]
            for j, cell in enumerate(row):
                neighbors = getNeighbors(i, j, last_row, curr_row)
                status = getCellStatus(cell, neighbors)
                board[i][j] = status
            last_row = [c for c in curr_row]

    # Time: O(m*n), Space: O(1)
    def gameOfLife3(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # all new 0's denotes as -1, (1 ==> 0)
        # all new 1's denotes as 2   (0 ==> 1)
        m, n = len(board), len(board[0])
        dirs = [[-1, -1], [-1, 0], [-1, 1], [0, 1],
                [1, 1], [1, 0], [1, -1], [0, -1]]
        for i in range(m):
            for j in range(n):
                livecount = 0
                for r, c in dirs:
                    nr, nc = i + r, j + c
                    # originally 1's
                    if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1:
                        livecount += 1
                if board[i][j] == 1:
                    if livecount < 2 or livecount > 3:
                        board[i][j] = -1
                else:
                    if livecount == 3:
                        board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
# board = [[1, 1], [1, 0]]
Solution().gameOfLife(board)
print(board)
