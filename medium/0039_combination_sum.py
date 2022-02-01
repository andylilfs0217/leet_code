from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        for i, candidate in enumerate(candidates):
            queue = [[candidate]]
            while len(queue) > 0:
                curr = queue.pop(0)
                if sum(curr) == target:
                    ans.append(curr)
                elif sum(curr) < target:
                    last = candidates.index(curr[-1])
                    for j in range(last, len(candidates)):
                        queue.append(curr + [candidates[j]])
        return ans
