from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prevSum = 0
        res = []
        for num in nums:
            prevSum += num
            res.append(prevSum)
        return res
