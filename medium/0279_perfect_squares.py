import math


class Solution:
    def numSquares(self, n: int) -> int:
        def getSquares(n):
            i = 1
            list_of_squares = []
            max_sq_root = math.floor(math.sqrt(n))
            while i <= max_sq_root:
                list_of_squares.append(i**2)
                i += 1
            return reversed(list_of_squares)
