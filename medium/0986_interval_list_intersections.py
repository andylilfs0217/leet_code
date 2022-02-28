from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n, m = len(firstList), len(secondList)
        i, j = 0, 0
        res = []
        while i < n and j < m:
            l, r = max(firstList[i][0], secondList[j][0]), min(
                firstList[i][1], secondList[j][1])
            if l <= r:
                res.append([l, r])
            if firstList[i][1] > secondList[j][1]:
                j += 1
            elif firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                i += 1
                j += 1
        return res


cases = [
    [[[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]],
    [[[1, 3], [5, 9]], []]
]

for case in cases:
    print(Solution().intervalIntersection(case[0], case[1]))
