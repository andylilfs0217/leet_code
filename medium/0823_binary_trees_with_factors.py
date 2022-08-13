from typing import List


class Solution:
    M = 10**9+7

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        return self.numFactoredBinaryTrees1(arr)

    # Dynamic programming. Time: O(n**2), Space: O(n)
    def numFactoredBinaryTrees1(self, arr: List[int]) -> int:
        arr = sorted(arr)
        res = 0
        dp = {}
        for i in range(len(arr)):
            num = arr[i]
            temp_res = 1
            for stored_num, stored_res in dp.items():
                if num % stored_num == 0 and (num//stored_num) in dp:
                    stored_res2 = dp[num//stored_num]
                    temp_res += stored_res * stored_res2
            dp[num] = temp_res
            res = (res + temp_res) % self.M
        return res % self.M


print(Solution().numFactoredBinaryTrees(arr=[2, 4]) == 3)
print(Solution().numFactoredBinaryTrees(arr=[2, 4, 5, 10]) == 7)
print(Solution().numFactoredBinaryTrees(arr=[8, 2, 4, 16]) == 23)
