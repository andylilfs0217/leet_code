from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # return self.combinationSum4_1(nums, target)
        # return self.combinationSum4_2(nums, target)
        return self.combinationSum4_3(nums, target)

    # Recursion. Time: O(nums.length*target), Space: O(target)
    def combinationSum4_1(self, nums: List[int], target: int) -> int:
        min_num = min(nums)

        def calResult(target: int) -> int:
            temp_res = 0
            if min_num > target:
                return temp_res
            for num in nums:
                if num == target:
                    temp_res += 1
                elif num < target:
                    temp_res += calResult(target-num)
            return temp_res

        res = calResult(target)
        return res

    # Memo.
    def combinationSum4_2(self, nums: List[int], target: int) -> int:
        min_num = min(nums)
        memo = {}

        def calResult(target: int) -> int:
            temp_res = 0
            if min_num > target:
                return temp_res
            temp_res = memo.get(target, 0)
            if temp_res > 0:
                return temp_res
            for num in nums:
                if num == target:
                    temp_res += 1
                elif num < target:
                    temp_res += calResult(target-num)
            memo[target] = temp_res
            return temp_res

        res = calResult(target)
        return res

    # Dynamic programming.
    def combinationSum4_3(self, nums: List[int], target: int) -> int:
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break
                combs[i] += combs[i - num]
        return combs[target]


print(Solution().combinationSum4(nums=[1, 2, 3], target=4) == 7)
print(Solution().combinationSum4(nums=[9], target=3) == 0)
print(Solution().combinationSum4(nums=[4, 2, 1], target=32))
