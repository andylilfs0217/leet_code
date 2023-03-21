import copy
from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.exist1(board, word)

    def exist1(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def is_out_of_bound(i: int, j: int) -> bool:
            return i < 0 or j < 0 or i >= m or j >= n

        def helper(i: int, j: int, s: str, visited: List[List[bool]]) -> bool:
            ans = False
            if board[i][j] == s[0]:
                visited[i][j] = True
                remain_s = s[1:]
                if len(remain_s) == 0:
                    ans = True
                    return ans
                for x, y in DIRS:
                    if not is_out_of_bound(
                            i + x, j + y) and not visited[i + x][j + y]:
                        new_visited = copy.deepcopy(visited)
                        ans = helper(i + x, j + y, remain_s, new_visited)
                        if ans:
                            return ans
            return ans

        ans = False
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                visited = [[False for _ in range(n)] for _ in range(m)]
                res = helper(i, j, word, visited)
                if res:
                    return res
        return ans


print(Solution().exist(board=[
    ["A", "B", "C", "E"],
    ["S", "F", "E", "S"],
    ["A", "D", "E", "E"],
],
                       word="ABCESEEEFS"))
print(Solution().exist(board=[["a"]], word="a"))
print(Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"],
                              ["A", "D", "E", "E"]],
                       word="ABCCED"))
print(Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"],
                              ["A", "D", "E", "E"]],
                       word="SEE"))
print(Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"],
                              ["A", "D", "E", "E"]],
                       word="ABCB"))
pass