class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        is_within_num = False
        l = 0
        numbers = set()
        for r, char in enumerate(word):
            if is_within_num and not (char >= '0' and char <= '9'):
                is_within_num = False
                numbers.add(int(word[l:r]))
            elif not is_within_num and char >= '0' and char <= '9':
                l = r
                is_within_num = True
        if is_within_num:
            numbers.add(int(word[l:]))
        count = len(numbers)
        return count
