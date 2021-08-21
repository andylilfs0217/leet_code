from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif target - numbers[j] < numbers[i]:
                j -= 1
            else:
                i += 1


Solution().twoSum([2, 7, 11, 15], 9)
