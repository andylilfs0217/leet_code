from typing import Counter, List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkHasRepeat(nums: List[str]):
            counter = Counter(nums)
            counter.pop('.')
            for count in counter.values():
                if count > 1:
                    return False
            return True
        n = 9
        valid = True
        for i in range(n):
            valid = valid and checkHasRepeat(board[i]) and checkHasRepeat([
                row[i] for row in board])
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                box = []
                for k in range(3):
                    row = board[i+k][j:j+3]
                    box += row
                valid = valid and checkHasRepeat(box)
        return valid
