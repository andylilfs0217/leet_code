from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest_money = 0
        for account in accounts:
            money = sum(account)
            if money > richest_money:
                richest_money = money
        return richest_money
