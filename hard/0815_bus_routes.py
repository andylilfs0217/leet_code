from typing import List


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], source: int,
                              target: int) -> int:
        return self.numBusesToDestination1(routes, source, target)

    def numBusesToDestination1(self, routes: List[List[int]], source: int,
                               target: int) -> int:
        return