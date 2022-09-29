from typing import List


class Solution:

    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        return self.findOrder1(numCourses, prerequisites)

    def findOrder1(self, numCourses: int,
                   prerequisites: List[List[int]]) -> List[int]:
        ans = []
        post_of = {}
        pre_of = {}
        for post, pre in prerequisites:
            pre_list = post_of.get(post, [])
            pre_list.append(pre)
            post_of[post] = pre_list

            post_list = pre_of.get(pre, [])
            post_list.append(post)
            pre_of[pre] = post_list

        # Search for cycle
        visited = set()
        for start, post_list in pre_of.items():
            if start in visited:
                continue
            stack = [(start, set())]
            while stack:
                node, temp_visited = stack.pop()
                if node in temp_visited:
                    return ans  # There is a cycle, return an empty list
                next_node_list = pre_of.get(node, [])
                temp_visited.add(node)
                if node in visited or not next_node_list:
                    visited = visited.union(temp_visited)
                    continue
                for next_node in next_node_list:
                    stack.append((next_node, set(temp_visited)))

        # Find topological sort
        queue = list(range(numCourses))
        visited = set()
        while queue:
            from_node = queue.pop(0)
            if from_node not in visited:
                if from_node not in pre_of and from_node not in post_of:
                    visited.add(from_node)
                    ans.append(from_node)
                elif from_node in pre_of and from_node not in post_of:
                    visited.add(from_node)
                    ans.append(from_node)
                    to_node_list = pre_of.get(from_node, [])
                    for to_node in to_node_list:
                        queue.append(to_node)
                        post_of.get(to_node, []).remove(from_node)
                        if post_of.get(to_node, []) == []:
                            post_of.pop(to_node, [])
                    pre_of.pop(from_node, [])
                    pass
            pass

        return ans


print(Solution().findOrder(numCourses=4,
                           prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
print(Solution().findOrder(numCourses=2, prerequisites=[[1, 0]]))
print(Solution().findOrder(numCourses=1, prerequisites=[]))
print(Solution().findOrder(numCourses=3,
                           prerequisites=[[0, 1], [1, 2], [2, 0]]))
