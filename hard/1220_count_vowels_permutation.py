class Solution:
    M = 10**9+7

    def countVowelPermutation(self, n: int) -> int:
        return self.countVowelPermutation1(n)

    # Dynamic programming. Time: O(n), Space: O(1)
    def countVowelPermutation1(self, n: int) -> int:
        if n == 1:
            return 5
        prev_dp = [1] * 5
        curr_dp = [0] * 5
        for _ in range(2, n+1):
            curr_dp[0] = prev_dp[1] + prev_dp[2] + prev_dp[4]
            curr_dp[1] = prev_dp[0] + prev_dp[2]
            curr_dp[2] = prev_dp[1] + prev_dp[3]
            curr_dp[3] = prev_dp[2]
            curr_dp[4] = prev_dp[2] + prev_dp[3]
            prev_dp = [cell for cell in curr_dp]
            curr_dp = [0] * 5
        res = sum(prev_dp)
        return res % self.M


print(Solution().countVowelPermutation(n=1) == 5)
print(Solution().countVowelPermutation(n=2) == 10)
print(Solution().countVowelPermutation(n=5) == 68)
