class Solution:
    # Newton method
    # def mySqrt(self, x: int) -> int:
    #     r = x
    #     while r*r > x:
    #         r = (r + x/r) / 2
    #     return int(r)

    # Binary search
    def mySqrt(self, x: int) -> int:
        left = 0
        right = 2**31 - 1
        while True:
            mid = left + (right - left) // 2
            if mid > x/mid:
                right = mid - 1
            else:
                if mid + 1 > x/(mid + 1):
                    return mid
                else:
                    left = mid + 1
