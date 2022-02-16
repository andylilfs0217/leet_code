from typing import Counter, List


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n, M = len(nextVisit), 10**9 + 7
        dp = [0]*n
        for i in range(1, n):
            dp[i] = (2*dp[i-1] - dp[nextVisit[i-1]] + 2) % M

        return dp[-1]
