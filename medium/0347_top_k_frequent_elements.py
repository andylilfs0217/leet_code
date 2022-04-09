from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return self.topKFrequent1(nums, k)
        return self.topKFrequent2(nums, k)

    # O(n) time and space
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        counter_map = Counter(nums)
        return [key for key, value in counter_map.most_common(k)]

    # Intuitive method
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        counter_map = {}
        for num in nums:
            counter_map[num] = counter_map.get(num, 0) + 1

        res = []
        heapq.heapify(res)
        for num, count in counter_map.items():
            if len(res) < k:
                heapq.heappush(res, (count, num))
            elif count > res[0][0]:
                heapq.heapreplace(res, (count, num))
        return [item[1] for item in res]
