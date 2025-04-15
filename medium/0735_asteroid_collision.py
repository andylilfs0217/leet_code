from typing import List
import collections


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def checkIsSameDir(prev, curr):
            return prev * curr > 0

        def willCollide(prev, curr):
            return prev > 0 and curr < 0

        def getWinningAst(prev, curr):
            if abs(prev) > abs(curr):
                return prev
            elif abs(prev) < abs(curr):
                return curr
            else:
                return None

        n = len(asteroids)
        mod_asts = asteroids
        stack = []
        for ast in mod_asts:
            stack.append(ast)
            while len(stack) >= 2:
                curr_ast = stack.pop()
                prev_ast = stack.pop()
                # Check if the direction is the same
                if checkIsSameDir(prev_ast, curr_ast) or not willCollide(
                    prev_ast, curr_ast
                ):
                    # If yes, add to stack
                    stack.append(prev_ast)
                    stack.append(curr_ast)
                    break
                else:
                    # If not, do compare
                    winningAst = getWinningAst(prev_ast, curr_ast)
                    if not winningAst:
                        # Both asts got destroyed
                        break
                    else:
                        # There is a winning ast, add it back the the queue
                        stack.append(winningAst)
        return stack


print(Solution().asteroidCollision([5, 10, -5]))  # [5,10]
print(Solution().asteroidCollision([8, -8]))  # []
print(Solution().asteroidCollision([10, 2, -5]))  # [10]
print(Solution().asteroidCollision([-5, 10, 8, -5, 5, -3, -7, 8]))  # [-5, 10, 8, 8]
