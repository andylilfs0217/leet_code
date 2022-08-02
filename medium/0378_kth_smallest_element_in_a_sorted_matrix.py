import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # return self.kthSmallest1(matrix, k)
        # return self.kthSmallest2(matrix, k)
        return self.kthSmallest3(matrix, k)

    # Priority queue. Time: O(m*n*log(m*n)), Space: O(n*m)
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        q = []
        for row in matrix:
            for cell in row:
                heapq.heappush(q, cell)
        return heapq.nsmallest(k, q)[-1]

    # Priority queue. Time: O(k*log(k)), Space: O(k)
    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        q = []  # val, r, c
        m, n = len(matrix), len(matrix[0])
        for r in range(min(k, m)):
            heapq.heappush(q, (matrix[r][0], r, 0))
        ans = -1
        for _ in range(k):
            ans, r, c = heapq.heappop(q)
            # Push the cell on the right
            if c+1 < n:
                heapq.heappush(q, (matrix[r][c+1], r, c+1))
        return ans

    # Binary search. Time: O((m+n)*log(max-min)), Space: O(1)
    def kthSmallest3(self, matrix: List[List[int]], k: int) -> int:
        # For general, the matrix need not be a square
        m, n = len(matrix), len(matrix[0])

        def countLessOrEqual(x):
            cnt = 0
            c = n - 1  # start with the rightmost column
            for r in range(m):
                while c >= 0 and matrix[r][c] > x:
                    c -= 1  # decrease column until matrix[r][c] <= x
                cnt += (c + 1)
            return cnt

        left, right = matrix[0][0], matrix[-1][-1]
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) >= k:
                ans = mid
                right = mid - 1  # try to looking for a smaller value in the left side
            else:
                left = mid + 1  # try to looking for a bigger value in the right side

        return ans


print(Solution().kthSmallest(
    matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8) == 13)
print(Solution().kthSmallest(matrix=[[-5]], k=1) == -5)
