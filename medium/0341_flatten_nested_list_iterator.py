# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

from typing import List


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.stack = nestedList[::-1]
        self.intList = []
        while self.stack:
            element = self.stack.pop()
            if element.isInteger():
                self.intList.append(element.getInteger())
            else:
                element_list = element.getList()
                for sub_element in element_list[::-1]:
                    self.stack.append(sub_element)
        self.idx = 0

    def next(self) -> int:
        res = self.intList[self.idx]
        self.idx += 1
        return res

    def hasNext(self) -> bool:
        return self.idx < len(self.intList)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
