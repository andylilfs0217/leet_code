from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        minIdx = maxIdx = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if minIdx == maxIdx:
                    ans.append(str(nums[maxIdx]))
                else:
                    ans.append(f'{nums[minIdx]}->{nums[maxIdx]}')
                minIdx = maxIdx = i
            else:
                maxIdx = i

        if minIdx == maxIdx:
            ans.append(str(nums[maxIdx]))
        else:
            ans.append(f'{nums[minIdx]}->{nums[maxIdx]}')

        return ans


Solution().summaryRanges()
