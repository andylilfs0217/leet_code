from typing import List


class Solution:
    MAX = 10**6 + 1

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # return self.findMedianSortedArrays1(nums1, nums2)
        return self.findMedianSortedArrays2(nums1, nums2)

    # Brute force. O(q log q) time, O(q) space
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        q = len(nums)
        return (nums[q//2 - 1 + q % 2] + nums[q//2]) / 2

    # O(q) time, O(1) space
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        while i+j <= (n+m)//2:
            num1 = nums1[i] if i < n else self.MAX
            num2 = nums2[j] if j < m else self.MAX
            if i+j == (n+m)//2-1+(n+m) % 2:
                l = min(num1, num2)
            if i+j == (n+m)//2:
                r = min(num1, num2)
            if num1 < num2:
                i += 1
            else:
                j += 1
        return (l+r)/2


print(Solution().findMedianSortedArrays([0, 0], [0, 0]))
