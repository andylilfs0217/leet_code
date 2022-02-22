from typing import List


class Solution:

    digit_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result_set = set((self.digit_map[digits[0]]))
        for digit in digits[1:]:
            temp_set = set(result_set)
            result_set.clear()
            while temp_set:
                comb = temp_set.pop()
                for char in self.digit_map[digit]:
                    new_comb = comb + char
                    result_set.add(new_comb)
        return list(result_set)


print(Solution().letterCombinations(''))
