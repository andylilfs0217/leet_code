# Strings [a], [b] are with the same length. Put a cut to [a] and [b] at the same index,
# where a = aprefix + asuffix
# b = bprefix + bsuffix
# aprefix.length == bprefix.length
# asuffix.length == bsuffix.length
# Write a function to check if aprefix+bsuffix or bprefix+asuffix is a palindrome.
# 0 <= a.length = b.length <= 10**5

import unittest


class Solution:
    def checkTwoStringPalindrome(self, a: str, b: str) -> bool:
        # return self.checkTwoStringPalindrome1(a, b)
        return self.checkTwoStringPalindrome2(a, b)

    # O(n^2) time, O(n) space
    def checkTwoStringPalindrome1(self, a: str, b: str) -> bool:
        for i, _ in enumerate(a):
            apre, asuf = a[:i], a[i:]
            bpre, bsuf = b[:i], b[i:]
            new1, new2 = apre+bsuf, bpre+asuf
            if self.checkPalindrome(new1) or self.checkPalindrome(new2):
                return True
        return False

    # O(n) time, O(n) space
    def checkTwoStringPalindrome2(self, a: str, b: str) -> bool:
        n = len(a)
        if n <= 1:
            return True
        l = n//2 - 1
        r = n//2 if n % 2 == 0 else n//2 + 1
        while l >= 0 and r < n and (a[l] == a[r] or b[l] == b[r]):
            l -= 1
            r += 1
        mid_part = a[l+1:r] if a[l+1] == a[r-1] else b[l+1:r]
        new1, new2 = a[:l+1]+mid_part+b[r:], b[:l+1]+mid_part+a[r:]
        return self.checkPalindrome(new1) or self.checkPalindrome(new2)

    def checkPalindrome(self, s: str) -> bool:
        return s == s[::-1]


# Example 1: "abcdef", "xxxcba" -> True
# Example 2: "abcdef", "xxxxba" -> True
# Example 3: "xxxcba", "abcxxx" -> True
# Example 4: "abcde", "xxxba" -> True
# Example 5: "abcde", "xxxxe" -> False
# Example 6: "", "" -> True
# Example 7: "xxxcba", "abcxxx" -> True
cases = [
    ["abcdef", "xxxcba"],
    ["abcdef", "xxxxba"],
    ["xxxcba", "abcxxx"],
    ["abcde", "xxxba"],
    ["abcde", "xxxxe"],
    ['', ''],
    ['xxxcba', 'abcdef']
]
solution = Solution()
for case in cases:
    print(solution.checkTwoStringPalindrome(case[0], case[1]))
