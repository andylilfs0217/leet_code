from typing import List


class Solution:
    # Time complexity = O(n^2)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(0, len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    # Time complexity = O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                j = hashMap[diff]
                return [i, j]
            else:
                hashMap[num] = i
