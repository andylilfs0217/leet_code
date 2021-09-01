from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for idx, num in enumerate(nums):
            if num not in hashMap or idx - hashMap[num] > k:
                hashMap[num] = idx
            else:
                return True
        return False
