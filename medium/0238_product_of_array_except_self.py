from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.productExceptSelf2(nums)

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

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        # left_prod_list = [1, -1, -1, 0, 0]
        # right_prod_list = [0, 0, -9, 3, 1]
        # res = [0, 0, 9, 0, 0]

        # left_prod_list = [1, 1, 2, 6]
        # right_prod_list = [24, 12, 4, 1]
        # res = [24, 12, 8, 6]

        left_prod_list, right_prod_list = [1], [1]
        for num in nums[:-1]:
            l = left_prod_list[-1]
            prod = l * num
            left_prod_list.append(prod)
        for num in nums[1:][::-1]:
            r = right_prod_list[0]
            prod = r * num
            right_prod_list.insert(0, prod)
        res = []
        for i, l_prod in enumerate(left_prod_list):
            r_prod = right_prod_list[i]
            prod = l_prod * r_prod
            res.append(prod)
        return res


print(Solution().productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6])
print(Solution().productExceptSelf(nums=[-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0])
