from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = buyIdx = 0
        j = sellIdx = len(prices) - 1
        buyPrice = prices[buyIdx]
        sellPrice = prices[sellIdx]
        while i < sellIdx or j > buyIdx:
            if prices[i] < buyPrice:
                buyPrice = prices[i]
                buyIdx = i
            if j > buyIdx:
                j -= 1
            if prices[j] > sellPrice:
                sellPrice = prices[j]
                sellIdx = j
            if i < sellIdx:
                i += 1
        return max(sellPrice - buyPrice, 0)


Solution().maxProfit(
    [2, 1, 2, 1, 0, 0, 1])
