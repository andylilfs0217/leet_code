from typing import List


class Solution:
    # Time O(n^2)
    # def maxProfit(self, prices: List[int]) -> int:
    #     result = 0
    #     for i in range(len(prices)):
    #         for j in range(i+1, len(prices)):
    #             result = max(result, prices[j] - prices[i])
    #     return result

    def maxProfit(self, prices: List[int]) -> int:
        maxCur = maxSoFar = 0
        for i in range(1, len(prices)):
            maxCur = max(0, prices[i] - prices[i-1] + maxCur)
            maxSoFar = max(maxSoFar, maxCur)
        return maxSoFar
