from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generateParenthesis1(n)

    def generateParenthesis1(self, n: int) -> List[str]:
        ans = []

        def backtrack(S=[], left=0, right=0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans


print(Solution().generateParenthesis(3) == [
      "((()))", "(()())", "(())()", "()(())", "()()()"])
print(Solution().generateParenthesis(1) == ["()"])
