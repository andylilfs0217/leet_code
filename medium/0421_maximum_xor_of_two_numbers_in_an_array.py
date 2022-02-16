from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # return self.findMaximumXOR1(nums)
        return self.findMaximumXOR2(nums)

    # O(n**2) time, O(1) space
    def findMaximumXOR1(self, nums: List[int]) -> int:
        max_xor = 0
        n = len(nums)
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                max_xor = max(max_xor, num1 ^ num2)
        return max_xor

    def findMaximumXOR2(self, nums: List[int]) -> int:
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)
        return answer
