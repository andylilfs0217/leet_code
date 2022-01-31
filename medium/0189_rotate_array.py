from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # self.rotate1(nums, k)
        # self.rotate2(nums, k)
        self.rotate3(nums, k)

    # O(n) space and time
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        new_nums = nums[-k:] + nums[:-k]
        for i, num in enumerate(new_nums):
            nums[i] = num

    # O(n*k) time, O(1) space
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        for _ in range(k):
            last = nums[-1]
            for i in range(n-1, 0, -1):
                nums[i] = nums[i-1]
            nums[0] = last

    # O(n) time, O(1) space
    def rotate3(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseNums(start: int, end: int) -> None:
            for i in range((end-start+1)//2):
                nums[start+i], nums[end-i] = nums[end-i], nums[start+i]

        n = len(nums)
        k %= n
        reverseNums(n-k, n-1)
        reverseNums(0, n-k-1)
        reverseNums(0, n-1)
