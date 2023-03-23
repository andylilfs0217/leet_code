import collections
from typing import List


class Solution:

    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        return self.canFinish1(numCourses, prerequisites)

    def canFinish1(self, numCourses: int,
                   prerequisites: List[List[int]]) -> bool:

        ans = True
        preSet = collections.defaultdict(list)
        for f, t in prerequisites:
            preSet[f].append(t)

        def notInCycle(num: int, visitedSet: set) -> bool:
            if num not in visitedSet and len(preSet[num]) == 0:
                return True
            elif num in visitedSet:
                return False
            visitedSet.add(num)
            for t in preSet[num]:
                res = notInCycle(t, set(visitedSet))
                if res:
                    preSet[num].remove(t)
                else:
                    return False
            return True

        for num in range(numCourses):
            res = notInCycle(num, set())
            if not res:
                ans = False
                break
        return ans


print(Solution().canFinish(numCourses=2, prerequisites=[[1, 0]]))
print(Solution().canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
print(Solution().canFinish(numCourses=3,
                           prerequisites=[[0, 1], [1, 2], [2, 0]]))
print(Solution().canFinish(numCourses=4,
                           prerequisites=[[0, 1], [1, 2], [2, 0], [3, 0]]))
print(Solution().canFinish(numCourses=5,
                           prerequisites=[[0, 2], [0, 1], [1, 3], [1, 4],
                                          [3, 4]]))
