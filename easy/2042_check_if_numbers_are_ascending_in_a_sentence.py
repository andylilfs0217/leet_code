class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s_list = s.split()
        prev = 0
        res = True
        for word in s_list:
            try:
                number = int(word)
                if number > prev:
                    prev = number
                    continue
                else: 
                    res = False
                    break
            except:
                continue
        return res
        