"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = {node: Node(node.val)}
        stack = [node]
        while stack:
            curr_node = stack.pop()
            for neigh in curr_node.neighbors:
                if neigh not in visited:
                    stack.append(neigh)
                    visited[neigh] = Node(neigh.val)
                visited[curr_node].neighbors.append(visited[neigh])
        return visited[node]
