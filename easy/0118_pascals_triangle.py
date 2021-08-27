from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
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
