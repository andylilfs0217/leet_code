class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # return self.removeDuplicates1(s, k)
        return self.removeDuplicates2(s, k)

    # Time: O(n*k), Space: O(n)
    def removeDuplicates1(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            stack.append(char)
            while len(stack) >= k and stack[-k:].count(stack[-1]) == k:
                stack = stack[:-k]
        return ''.join(stack)

    # Time: O(n), Space: O(n)
    def removeDuplicates2(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if len(stack) > 0 and char == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            stack[-1][1] %= k
            if stack[-1][1] == 0:
                stack.pop()
        # char_stack = []
        # for element in stack:
        #     for _ in range(element[1]):
        #         char_stack.append(element[0])
        char_stack = [char * count for char, count in stack]
        return ''.join(char_stack)


print(Solution().removeDuplicates(s="pbbcggttciiippooaais", k=2))
