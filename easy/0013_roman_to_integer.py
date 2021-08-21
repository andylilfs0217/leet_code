class Solution:
    def romanToInt(self, s: str) -> int:
        roman_val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num = 0
        str_len = len(s)
        idx = 0
        while idx < str_len:
            char = s[idx]
            if idx == str_len - 1:
                # If the char is at the last index
                num += roman_val[char]
                return num
            if idx == str_len - 2 and roman_val[char] < roman_val[s[idx+1]]:
                # If the char is at the 2nd last index and it is compound roman value
                num += roman_val[s[idx+1]] - roman_val[char]
                return num
            if roman_val[char] < roman_val[s[idx+1]]:
                # If it is compound roman value
                num += roman_val[s[idx+1]] - roman_val[char]
                idx += 1
            else:
                num += roman_val[char]
            idx += 1
