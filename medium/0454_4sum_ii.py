from typing import List


class Solution:
    # O(n^4) solutions
    # def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    #     count = 0
    #     for i in nums1:
    #         for j in nums2:
    #             for k in nums3:
    #                 for l in nums4:
    #                     if i + j + k + l == 0:
    #                         count += 1
    #     return count

    # O(n^2) solutions
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        hash_map = {}
        for i in nums1:
            for j in nums2:
                hash_map[i+j] = 1 if i + \
                    j not in hash_map else hash_map[i+j] + 1
        for k in nums3:
            for l in nums4:
                if -k-l in hash_map:
                    count += hash_map[-k-l]
        return count
