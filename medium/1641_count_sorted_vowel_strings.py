from math import comb


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return self.countVowelStrings1(n)

    # Time: O(5n), Space: O(1)
    def countVowelStrings1(self, n: int) -> int:
        arr = [0, 0, 0, 0, 1]
        for _ in range(n):
            total = sum(arr)
            for j in range(5):
                temp = total
                total -= arr[j]
                arr[j] = temp
        return sum(arr)

    # Time: O(1), Space: O(n)
    def countVowelStrings2(self, n: int) -> int:
        return comb(n+4, 4)


print(Solution().countVowelStrings(50))
