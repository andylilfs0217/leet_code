from typing import List


class Solution:
    # Dynamic programming
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        ans = [0]*n
        mx = [0]*n
        for i in range(n-1, -1, -1):
            pts, skip = questions[i]
            if i + skip + 1 < n:
                ans[i] = mx[i+skip+1] + pts
            else:
                ans[i] = pts
            mx[i] = ans[i] if i == n-1 else max(mx[i+1], ans[i])
        return max(ans)
