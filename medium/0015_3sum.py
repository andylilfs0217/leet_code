from collections import Counter
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.threeSum1(nums)

    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        keys = list(counter)
        n = len(keys)
        res = []
        for i in range(n):
            for j in range(i, n):
                key_i, key_j = keys[i], keys[j]
                counter[key_i] -= 1
                counter[key_j] -= 1
                key_k = 0-key_i-key_j
                if counter.get(key_k, 0) > 0 and counter[key_j] >= 0:
                    res.append([key_i, key_j, key_k])
                counter[key_i] += 1
                counter[key_j] += 1
        return res


print(Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))
