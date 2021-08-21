from typing import List


class Solution:
    # O(n) time complexity and O(n) space complexity
    # def majorityElement(self, nums: List[int]) -> int:
    #     map = {}
    #     for num in nums:
    #         map[num] = 1 if num not in map else map[num] + 1
    #     max = 0
    #     for key, val in map.items():
    #         if val > max:
    #             result = key
    #             max = val
    #     return result

    # O(n) time complexity and O(1) space complexity
    # def majorityElement(self, nums: List[int]) -> int:
    #     count = 1
    #     majority = nums[0]
    #     for i in range(1, len(nums)):
    #         if count == 0:
    #             count += 1
    #             majority = nums[i]
    #         elif majority == nums[i]:
    #             count += 1
    #         else:
    #             count -= 1
    #     return majority

    # Using function
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
