from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        for num in nums:
            if not stack or stack[-1][0] > num:
                stack.append([num, num])
            elif num > stack[-1][0]:
                last = stack.pop()
                if last[1] > num:
                    return True
                last[1] = num
                while stack and stack[-1][1] <= num:
                    stack.pop()
                if stack and stack[-1][0] < num:
                    return True
                stack.append(last)
        return False
