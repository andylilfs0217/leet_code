class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_num = str(x)
        str_len = len(str_num)
        for i in range(0, str_len//2):
            if str_num[i] != str_num[str_len - 1 - i]:
                return False
        return True
