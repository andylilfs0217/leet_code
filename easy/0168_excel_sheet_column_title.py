class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columnName = ''
        while columnNumber > 0:
            curr = columnNumber % 26
            columnNumber //= 26
            if curr == 0:
                curr = 26
                columnNumber -= 1
            columnName = self.convertToName(curr) + columnName
        return columnName

    def convertToName(self, number: int) -> str:
        char = chr(number + 64)
        return char


Solution().convertToTitle(701)
