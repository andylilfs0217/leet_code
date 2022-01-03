from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash_map = {}
        for num in arr:
            hash_map[num] = 1 if num not in hash_map else hash_map[num] + 1
        res = -1
        for key, val in hash_map.items():
            if key == val and key > res:
                res = key
        return res
