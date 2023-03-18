import heapq

# addNum() -> O(log(n))
# findMedian() -> O(n log(k))

# class MedianFinder:

#     def __init__(self):
#         self.nums = []
#         return

#     def addNum(self, num: int) -> None:
#         heapq.heappush(self.nums, num)
#         pass

#     def findMedian(self) -> float:
#         if len(self.nums) % 2 == 1:
#             ans = heapq.nsmallest(len(self.nums) // 2 + 1, self.nums)[-1] / 1
#             return ans
#         elif len(self.nums) == 0:
#             return None
#         else:
#             ans = sum(
#                 heapq.nsmallest(len(self.nums) // 2 + 1, self.nums)[-2:]) / 2
#             return ans


# addNum() -> O(log(n))
# findMedian() -> O(1)
class MedianFinder:

    def __init__(self):
        self.first_half, self.second_half = [], []

    def addNum(self, num: int) -> None:
        if len(self.first_half) == len(self.second_half):
            if len(self.first_half) == 0 or num <= self.second_half[0]:
                heapq.heappush(self.first_half, -num)
            else:
                median_right = heapq.heappop(self.second_half)
                heapq.heappush(self.first_half, -median_right)
                heapq.heappush(self.second_half, num)
        else:
            if num < -self.first_half[0]:
                median_left = -heapq.heappop(self.first_half)
                heapq.heappush(self.second_half, median_left)
                heapq.heappush(self.first_half, -num)
            else:
                heapq.heappush(self.second_half, num)

    def findMedian(self) -> float:
        if len(self.first_half) == 0:
            return None
        elif len(self.second_half) == 0:
            return -self.first_half[0]
        elif (len(self.first_half) + len(self.second_half)) % 2 == 0:
            return (-self.first_half[0] + self.second_half[0]) / 2
        else:
            return -self.first_half[0]


input_list = [
    40, 12, 16, 14, 35, 19, 34, 35, 28, 35, 26, 6, 8, 2, 14, 25, 25, 4, 33, 18,
    10, 14, 27, 3, 35, 13, 24, 27, 14, 5, 0, 38, 19, 25, 11, 14, 31, 30, 11,
    31, 0
]
medianFinder = MedianFinder()
for num in input_list:
    medianFinder.addNum(num)
    print(medianFinder.findMedian())