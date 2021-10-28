from typing import List


class Solution:
    # O(n log n) solution
    # def calBits(self, n: int):
    #     result = 0
    #     while n > 0:
    #         result += n % 2
    #         n //= 2
    #     return result

    # def countBits(self, n: int) -> List[int]:
    #     result = []
    #     for i in range(n+1):
    #         result.append(self.calBits(i))
    #     return result

    # O(n) solution

    def countBits(self, n: int) -> List[int]:
        result = [0]
        repeated_list = [0]
        curr = 0
        mul = 1
        while curr + mul <= n:
            curr += mul
            mul *= 2

            temp_list = list(map(lambda x: x + 1, repeated_list))
            result = result + temp_list
            repeated_list = result

        start = 0
        end = n-curr
        temp_list = list(map(lambda x: x+1, repeated_list[start:end]))
        result += temp_list

        return result
