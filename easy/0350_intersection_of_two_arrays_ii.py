from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        short = nums1 if len(nums1) < len(nums2) else nums2
        long = nums1 if len(nums1) >= len(nums2) else nums2
        count_map = {}
        result = []
        for num in short:
            count_map[num] = 1 if num not in count_map else count_map[num] + 1
        for num in long:
            if num in count_map and count_map[num] > 0:
                result.append(num)
                count_map[num] -= 1
        return result


Solution().intersect([1, 2, 2, 1], [2, 2])
