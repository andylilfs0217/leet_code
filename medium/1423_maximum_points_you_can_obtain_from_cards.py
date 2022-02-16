from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        last_sum = sum(cardPoints[:n-k])
        min_window = last_sum
        l, r = 1, n-k
        while r < n:
            last_sum = last_sum - cardPoints[l-1] + cardPoints[r]
            min_window = min(min_window, last_sum)
            l += 1
            r += 1
        return total_sum - min_window
