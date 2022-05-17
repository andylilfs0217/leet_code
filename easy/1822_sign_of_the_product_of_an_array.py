from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        is_negative = False
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                is_negative = not is_negative
        return 1 if not is_negative else -1
