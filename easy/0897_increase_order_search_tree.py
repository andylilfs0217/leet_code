# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # return self.increasingBST1(root)
        return self.increasingBST2(root)

    # Time: O(n), Space: O(h), recursion
    def increasingBST1(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            l1, r2 = node, node

            if node.left:
                l1, l2 = dfs(node.left)
                l2.right = node

            if node.right:
                r1, r2 = dfs(node.right)
                node.right = r1

            node.left = None
            return (l1, r2)

        return dfs(root)[0]

    # Time: O(n), Space: O(n), iteration
    def increasingBST2(self, root: TreeNode) -> TreeNode:
        stack = [root]
        values = []
        while stack:
            node = stack.pop()
            if node == None:
                continue
            if type(node) is int:
                values.append(TreeNode(node))
                continue
            stack.append(node.right)
            stack.append(node.val)
            stack.append(node.left)
        for i in range(len(values) - 1):
            values[i].right = values[i + 1]
        return values[0]
