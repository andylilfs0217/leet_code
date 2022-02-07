from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        buy_price = prices[0]
        n = len(prices)
        for i in range(1, n):
            curr_price = prices[i]
            if curr_price < buy_price:
                buy_price = curr_price
            elif curr_price > buy_price + fee:
                profit += curr_price - buy_price - fee
                buy_price = curr_price - fee
        return profit
