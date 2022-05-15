class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high % 2 == 0:
            high -= 1
        if low % 2 == 0:
            low += 1
        return (high-low)//2 + 1
