from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.productExceptSelf1(nums)

    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        products = []
        total, totalWithoutZero, numOfZero = 1, 1, 0
        for num in nums:
            total *= num
            if num != 0:
                totalWithoutZero *= num
            else:
                numOfZero += 1
        for num in nums:
            if numOfZero > 1:
                res = 0
            elif numOfZero == 0:
                res = total // num
            elif numOfZero == 1 and num == 0:
                res = totalWithoutZero
            else:
                res = 0

            products.append(res)

        return products


print(Solution().productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6])
print(Solution().productExceptSelf(nums=[-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0])
