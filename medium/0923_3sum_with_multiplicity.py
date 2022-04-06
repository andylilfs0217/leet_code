from collections import Counter
import itertools
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        DIVIDER = 10**9+7
        counter_map = Counter(arr)
        result = 0
        for i, j in itertools.combinations_with_replacement(counter_map, 2):
            k = target - i - j
            if i == j == k:
                result += counter_map[i] * \
                    (counter_map[i]-1) * (counter_map[i]-2) // 6
            elif i == j != k:
                result += counter_map[i] * \
                    (counter_map[i]-1) // 2 * counter_map[k]
            elif k > i and k > j:
                result += counter_map[i] * counter_map[j] * counter_map[k]
        return result % DIVIDER
