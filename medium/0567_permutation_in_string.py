from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        n1 = len(s1)
        curr_counter = Counter(s2[:n1])
        if self.compareCounter(counter, curr_counter):
            return True
        l = 0
        for r in range(n1, len(s2)):
            char_r = s2[r]
            char_l = s2[l]
            curr_counter[char_l] -= 1
            l += 1
            curr_counter[char_r] = curr_counter.get(char_r, 0) + 1
            if self.compareCounter(counter, curr_counter):
                return True
        return False

    def compareCounter(self, a: Counter, b: Counter):
        for char in a:
            count = a[char]
            if count != b.get(char, -1):
                return False
        return True
