# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.getTargetCopy1(original, cloned, target)

    def getTargetCopy1(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = [original]
        cloned_queue = [cloned]
        for i, original_node in enumerate(queue):
            if original_node:
                cloned_node = cloned_queue[i]
                if original_node == target:
                    return cloned_queue[i]
                queue.append(original_node.left)
                cloned_queue.append(cloned_node.left)
                queue.append(original_node.right)
                cloned_queue.append(cloned_node.right)
