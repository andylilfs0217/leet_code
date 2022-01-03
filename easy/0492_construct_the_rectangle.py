from typing import List
import math


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        optimum = round(math.sqrt(area))
        while area % optimum != 0:
            optimum -= 1

        return [area // optimum, optimum]
