from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # return self.generate1(numRows)
        return self.generate2(numRows)

    def generate1(self, numRows: int) -> List[List[int]]:
        lastRow = []
        result = []
        for i in range(numRows):
            thisRow = []
            for j in range(i+1):
                if j == 0 or j == i:
                    thisRow.append(1)
                else:
                    thisRow.append(lastRow[j-1] + lastRow[j])
            result.append(thisRow)
            lastRow = thisRow
        return result

    def generate2(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows == 1:
            return result
        for n in range(2, numRows+1):
            a, b = result[-1] + [0], [0] + result[-1]
            curr_row = []
            for i in range(len(a)):
                curr_cell = a[i] + b[i]
                curr_row.append(curr_cell)
            result.append(curr_row)
        return result
