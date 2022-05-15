from collections import defaultdict
import heapq
import math
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # return self.networkDelayTime1(times, n, k)
        # return self.networkDelayTime2(times, n, k)
        return self.networkDelayTime3(times, n, k)

    # BFS. Time: O(n*e), Space: O(n*e)
    # Using queue
    def networkDelayTime1(self, times: List[List[int]], n: int, k: int) -> int:
        paths = {}
        for time in times:
            path = paths.get(time[0], [])
            path.append(time)
            paths[time[0]] = path
        distances = [math.inf for _ in range(n+1)]
        distances[0] = 0
        stack = [[0, k, 0]]
        while stack:
            u, v, w = stack.pop(0)
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
                stack += paths.get(v, [])
        max_distance = max(distances)
        return max_distance if max_distance < math.inf else -1

    # DFS. Time: O((n-1)!+e log e), Space: O(n+e)
    # Using stack
    def networkDelayTime2(self, times: List[List[int]], n: int, k: int) -> int:
        paths = {}
        for time in times:
            path = paths.get(time[0], [])
            path.append(time)
            paths[time[0]] = path
        distances = [math.inf for _ in range(n+1)]
        distances[0] = 0
        stack = [[0, k, 0]]
        while stack:
            u, v, w = stack.pop()
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
                stack += paths.get(v, [])
        max_distance = max(distances)
        return max_distance if max_distance < math.inf else -1

    # Dijkstra. Time: O(n+e log n), Space: O(n+e)
    # Using priority queue/heap
    def networkDelayTime3(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, c in times:
            graph[src].append((dst, c))
        queue = [(0, k)]  # (cost, node)
        visited = set()
        max_cost = 0
        while queue:
            # Always pop the min value
            cost, node = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            max_cost = max(max_cost, cost)
            neighbours = graph[node]
            for neighbour in neighbours:
                new_node, new_cost = neighbour
                if new_node not in visited:
                    curr_cost = cost + new_cost
                    heapq.heappush(queue, (curr_cost, new_node))
        return max_cost if len(visited) == n else -1


print(Solution().networkDelayTime(
    times=[[1, 2, 2], [1, 3, 1], [1, 4, 4], [3, 5, 3], [4, 6, 1]], n=6, k=1))
