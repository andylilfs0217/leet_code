import math
from typing import List


class Solution:

    def successfulPairs(self, spells: List[int], potions: List[int],
                        success: int) -> List[int]:

        def binarySearch(potions: List[int], target: int) -> int:
            l, r = 0, len(potions)
            while l < r:
                mid = (l + r) // 2
                potion = potions[mid]
                if target >= potion:
                    l = mid + 1
                else:
                    r = mid
            return r

        for i, potion in enumerate(potions):
            potions[i] = math.ceil(success / potion)
        potions.sort()
        print(potions)

        ans = []
        for spell in spells:
            res = binarySearch(potions, spell)
            ans.append(res)
        return ans


print(Solution().successfulPairs(spells=[5, 1, 3],
                                 potions=[1, 2, 3, 4, 5],
                                 success=7))

print(Solution().successfulPairs(spells=[3, 1, 2],
                                 potions=[8, 5, 8],
                                 success=16))
