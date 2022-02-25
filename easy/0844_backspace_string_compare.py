class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.backspaceCompare1(s, t)

    # O(n) time, O(n) space
    def backspaceCompare1(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []
        for char in s:
            if char == '#' and len(stack1) > 0:
                stack1.pop(-1)
            elif char != '#':
                stack1.append(char)
        for char in t:
            if char == '#' and len(stack2) > 0:
                stack2.pop(-1)
            elif char != '#':
                stack2.append(char)
        return stack1 == stack2

    # TODO: O(n) time, O(1) space
    def backspaceCompare2(self, s: str, t: str) -> bool:
        back_s, back_t = 0, 0
        i, j = len(s)-1, len(t)-1
        while i >= 0 or j >= 0:
            char_s = s[i] if i >= 0 else '_'
            char_t = t[j] if j >= 0 else '_'
            if back_s == 0 and back_t == 0 and char_s != char_t and char_s != '#':
                return False
            if back_s > 0 and char_s != '#':
                back_s -= 1
                i -= 1
            if back_t > 0 and char_t != '#':
                back_t -= 1
                j -= 1

        return True


cases = [["ab#c", "ad#c"], ["ab##", "c#d#"], ["a#c", "b"]]
for case in cases:
    print(Solution().backspaceCompare(case[0], case[1]))
