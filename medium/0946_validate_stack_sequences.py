from typing import List


class Solution:

    def validateStackSequences(self, pushed: List[int],
                               popped: List[int]) -> bool:
        stack = []
        i, j = 0, 0
        invalid = False
        while not invalid and (i < len(pushed) or j < len(popped)):
            try:
                if not stack:
                    stack.append(pushed[i])
                    i += 1
                elif stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
                else:
                    stack.append(pushed[i])
                    i += 1
            except:
                invalid = True
        return not invalid