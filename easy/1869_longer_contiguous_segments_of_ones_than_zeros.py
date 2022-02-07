class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        long1s, long0s = 0, 0
        curr1s, curr0s = 0, 0
        isStreak1 = s[0] == '1'
        for char in s:
            if char == '1' and isStreak1:
                curr1s += 1
            elif char == '1' and not isStreak1:
                long0s = max(long0s, curr0s)
                curr0s = 0
                curr1s = 1
                isStreak1 = not isStreak1
            elif char == '0' and not isStreak1:
                curr0s += 1
            elif char == '0' and isStreak1:
                long1s = max(long1s, curr1s)
                curr1s = 0
                curr0s = 1
                isStreak1 = not isStreak1
        long1s = max(long1s, curr1s)
        long0s = max(long0s, curr0s)
        return long1s > long0s
