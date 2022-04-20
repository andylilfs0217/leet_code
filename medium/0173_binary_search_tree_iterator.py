# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        # self.__init__1(root)
        self.__init__2(root)

    # Space: O(n)
    def __init__1(self, root: Optional[TreeNode]):
        self.root = root
        self.tree = self.inorder(root)
        self.treeLen = len(self.tree)
        self.curr = 0

    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = self.inorder(root.left) + [root.val] + self.inorder(root.right)
        return res

    # Space: O(h)
    def __init__2(self, root: Optional[TreeNode]):
        self.stack: List[TreeNode] = []
        self.pushAll(root)

    def pushAll(self, root: Optional[TreeNode]) -> None:
        while root is not None:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        # return self.next1()
        return self.next2()

    # Time: O(1)
    def next1(self) -> int:
        res = self.tree[self.curr]
        self.curr += 1
        return res

    # Time: O(1)
    def next2(self) -> int:
        tempNode = self.stack.pop()
        self.pushAll(tempNode.right)
        return tempNode.val

    def hasNext(self) -> bool:
        # return self.hasNext1()
        return self.hasNext2()

    # Time: O(1)
    def hasNext1(self) -> bool:
        res = self.curr < self.treeLen
        return res

    # Time: O(1)
    def hasNext2(self) -> bool:
        return self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
root = TreeNode(7,
                TreeNode(3),
                TreeNode(15,
                         TreeNode(9),
                         TreeNode(20)))
obj = BSTIterator(root)
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
