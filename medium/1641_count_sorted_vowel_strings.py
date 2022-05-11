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
        """
        Following the lead from the article mentioned above, the problem asks us to pick n letters with repetition from "a, e, i, o, u" without permutation (without permutation is because the pick must be in order). Let's say n = 3, it can be

        a | e | i | o | u
        1 | 1 | 1 |   |
        or

        a | e | i | o | u
        | 2 |   | 1 |
        Notice the use of | as separators between letters. If we use a generic "x" to indicate the position a letter is picked, and also give all the | separators positions as well, the two options shown above can be written as:

        x | x | x | |
        _ _ _ _ _ _ _
        and

        | x x | | x |
        _ _ _ _ _ _ _
        Essentially, we have transformed the problem into finding how many ways we can put three "x" in seven positions. Extending this idea further, the original question is equivalent to asking how many ways we can put n "x" in n + 5 - 1 positions (think of 5 - 1 as the number of positions for separators and n the number of positions for "x"). The solution is simple: (n + 4) choose n, which is equivalent to (n + 4) choose 4.
        """
        return comb(n+4, 4)


print(Solution().countVowelStrings(50))
