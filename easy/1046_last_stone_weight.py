from typing import List


class Solution:
    # O(n^2) time
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max1 = stones.pop(stones.index(max(stones)))
            max2 = stones.pop(stones.index(max(stones)))
            if max1 > max2:
                stones.append(max1 - max2)
        return stones[0] if len(stones) == 1 else 0
