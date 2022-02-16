from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        cost.reverse()
        count = 0
        n = len(cost)
        for i in range(0, n, 3):
            count += cost[i]
            count += cost[i + 1] if i+1 < n else 0
        return count
