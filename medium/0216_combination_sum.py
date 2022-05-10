from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.combinationSum31(k, n, 1)

    def combinationSum31(self, k: int, n: int, l: int) -> List[List[int]]:
        smallest = (1+k)*k/2
        largest = ((9-k+1)+9)*k/2
        if n < smallest or n > largest:
            return []
        if k == 1 and n >= l:
            return [[n]]
        res = []
        for i in range(l, 10):
            if n-i < i + 1:
                break
            next_k, next_n, next_l = k-1, n-i, i+1
            tail = self.combinationSum31(next_k, next_n, next_l)
            if tail:
                res += [[i] + tail_element for tail_element in tail]
        return res


print(Solution().combinationSum3(k=9, n=45))
