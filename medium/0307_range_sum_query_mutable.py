from typing import List, Optional


class TreeNode:
    def __init__(self, range: List[int], val=0, left=None, right=None) -> None:
        self.val = val
        self.range = range
        self.left = left
        self.right = right


class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_nums = [0]
        for num in nums:
            self.sum_nums.append(num+self.sum_nums[-1])
        self.sum_nums.pop(0)

        def makeTree(index_range: List[int]):
            curr_val = self.sum_nums[index_range[1]] - \
                (self.sum_nums[index_range[0] - 1]
                 if index_range[0] > 0 else 0)
            if index_range[1] == index_range[0]:
                return TreeNode(index_range, curr_val)
            mid = (index_range[1] + index_range[0]) // 2
            return TreeNode(index_range,
                            curr_val,
                            makeTree([index_range[0], mid]),
                            makeTree([mid+1, index_range[1]]))

        length = len(nums)
        self.index_tree = makeTree([0, length-1])

    def update(self, index: int, val: int) -> None:
        stack = [self.index_tree]
        while stack:
            index_node = stack[-1]
            if index_node.range[0] == index_node.range[1]:
                break
            mid = (index_node.range[1] + index_node.range[0]) // 2
            if index <= mid:
                stack.append(index_node.left)
            else:
                stack.append(index_node.right)
        difference = val - stack[-1].val
        while stack:
            index_node = stack.pop()
            index_node.val += difference

    def sumRange(self, left: int, right: int) -> int:
        stack = [(self.index_tree, left, right)]
        total = 0
        while stack:
            index_node, l, r = stack.pop()
            if index_node.range == [l, r]:
                total += index_node.val
            else:
                mid = (index_node.range[0] + index_node.range[1]) // 2
                if l <= mid and r <= mid:
                    stack.append((index_node.left, l, r))
                elif l > mid and r > mid:
                    stack.append((index_node.right, l, r))
                else:
                    stack.append((index_node.left, l, mid))
                    stack.append((index_node.right, mid+1, r))
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# obj = NumArray([1, 3, 5])
# param_2 = obj.sumRange(0, 2)
# print(param_2 == 9)
# obj.update(1, 2)
# param_2 = obj.sumRange(0, 2)
# print(param_2 == 8)

obj = NumArray([0, 9, 5, 7, 3])
print(obj.sumRange(4, 4) == 3)
print(obj.sumRange(2, 4) == 15)
print(obj.sumRange(3, 3) == 7)
obj.update(4, 5)
obj.update(1, 7)
obj.update(0, 8)
print(obj.sumRange(1, 2) == 12)
obj.update(1, 9)
print(obj.sumRange(4, 4) == 5)
obj.update(3, 4)
for i in range(len(obj.sum_nums)):
    print(obj.sumRange(i, i))
