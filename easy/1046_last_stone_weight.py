from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # return self.lastStoneWeight1(stones)
        return self.lastStoneWeight2(stones)

    # O(n^2) time
    def lastStoneWeight1(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max1 = stones.pop(stones.index(max(stones)))
            max2 = stones.pop(stones.index(max(stones)))
            if max1 > max2:
                stones.append(max1 - max2)
        return stones[0] if len(stones) == 1 else 0

    # O(n log n) time
    def lastStoneWeight2(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            max1 = stones.pop()
            max2 = stones.pop()
            if max1 > max2:
                left = max1 - max2
                appended = False
                i = 0
                while not appended and i < len(stones):
                    if stones[i] > left:
                        stones.insert(i, left)
                        appended = True
                    i += 1
                if not appended:
                    stones.append(left)
        return stones[0] if len(stones) == 1 else 0


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
