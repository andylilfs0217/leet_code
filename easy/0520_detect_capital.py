class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        isAllCap = False
        isAllLow = False
        isTitle = False
        for i, char in enumerate(word):
            if i == 0:
                if char.islower():
                    isAllLow = True
                else:
                    isAllCap = True
                    isTitle = True
            elif i == 1:
                if isAllCap and char.islower():
                    isAllCap = False
                elif char.isupper():
                    isTitle = False
                    isAllLow = False
            elif char.islower():
                isAllCap = False
            elif char.isupper():
                isTitle = False
                isAllLow = False
        return isAllCap or isTitle or isAllLow
