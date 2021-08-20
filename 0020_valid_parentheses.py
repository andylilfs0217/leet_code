class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        stack = []
        for char in s:
            if char in parentheses.keys():
                stack.append(parentheses[char])
            else:
                if not stack:
                    return False
                last = stack.pop()
                if char != last:
                    return False
        if stack:
            return False
        return True


Solution().isValid('()')
