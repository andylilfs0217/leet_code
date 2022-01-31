class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            getBottles = emptyBottles // numExchange
            remain = emptyBottles % numExchange
            count += getBottles
            emptyBottles = remain + getBottles
        return count
