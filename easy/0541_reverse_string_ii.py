class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverseSubstring(s: str) -> str:
            i = 0
            j = len(s) - 1
            result = list(s)
            while i < j:
                temp = result[i]
                result[i] = result[j]
                result[j] = temp
                i += 1
                j -= 1
            return ''.join(result)

        length = len(s)
        i = 0
        result = ''
        while i < length:
            substring = s[i:min(i+k, length)]
            result += reverseSubstring(substring)
            i += k
            if i < length:
                substring = s[i:min(i+k, length)]
                result += substring
                i += k
        return result
