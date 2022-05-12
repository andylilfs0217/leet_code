from typing import Counter, List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # return self.permuteUnique1(nums)
        return self.permuteUnique2(nums)

    # Backtracking
    def permuteUnique1(self, nums: List[int]) -> List[List[int]]:
        def helper(path: List[int], counter: Counter):
            if len(path) == len(nums):
                ans.append(path[:])
            for num in counter.keys():
                if counter[num] > 0:
                    counter[num] -= 1
                    path.append(num)
                    helper(path, counter)
                    path.pop()
                    counter[num] += 1
        ans = []
        counter = Counter(nums)
        path = []
        helper(path, counter)
        return ans

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i < len(l) and l[i] == n:
                        break  # handles duplication
            ans = new_ans
        return ans


print(Solution().permuteUnique([1, 1, 2]))
