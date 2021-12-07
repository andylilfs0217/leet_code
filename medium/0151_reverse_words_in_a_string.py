class Solution:
    # O(n) space
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(' ')
        words = list(filter(lambda x: len(x) != 0, words))
        i = 0
        j = len(words) - 1
        while i < j:
            temp = words[i].strip()
            words[i] = words[j].strip()
            words[j] = temp
            i += 1
            j -= 1
        s = ' '.join(words)
        return s

    # O(1) space
    # def reverseWords(self, s: str) -> str:
    #     def reverseString(s: str) -> str:
    #         s = list(s)
    #         i = 0
    #         j = len(s) - 1
    #         while i < j:
    #             temp = s[i]
    #             s[i] = s[j]
    #             s[j] = temp
    #             i += 1
    #             j -= 1
    #         s = ''.join(s)

    #     def

    #     s = reverseString(s)
