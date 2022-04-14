from typing import List


class Solution:
    # Time: O(n), Space: O(1)
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n, score, max_score = len(nums), 0, 0
        nums.insert(0, 0)
        for i in range(1, n+1):
            score += 1 if nums[i] == 0 else -1
            nums[i] = score
            max_score = max(max_score, score)
        return [i for i, score in enumerate(
            nums) if score == max_score]
