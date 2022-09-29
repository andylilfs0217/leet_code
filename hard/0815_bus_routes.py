from typing import List


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], source: int,
                              target: int) -> int:
        # return self.numBusesToDestination1(routes, source, target)
        return self.numBusesToDestination2(routes, source, target)

    # TLE
    def numBusesToDestination1(self, routes: List[List[int]], source: int,
                               target: int) -> int:
        # Create a graph
        from_to_edges = {}
        for route in routes:
            for from_node in route:
                for to_node in route:
                    if from_node != to_node:
                        to_list = from_to_edges.get(from_node, [])
                        to_list.append(to_node)
                        from_to_edges[from_node] = to_list

        queue = [(source, 0)]
        visited = set()
        while queue:
            from_node, curr_dist = queue.pop(0)
            if from_node == target:
                return curr_dist
            visited.add(from_node)
            curr_dist += 1
            to_list = from_to_edges.get(from_node, [])
            for to_node in to_list:
                if to_node == target:
                    return curr_dist
                elif to_node not in visited:
                    queue.append((to_node, curr_dist))
        return -1

    def numBusesToDestination2(self, routes: List[List[int]], source: int,
                               target: int) -> int:
        node_to_bus_map = {}
        for bus, route in enumerate(routes):
            for stop in route:
                bus_list = node_to_bus_map.get(stop, [])
                bus_list.append(bus)
                node_to_bus_map[stop] = bus_list
        from_to_bus_edges = {}
        for buses in node_to_bus_map.values():
            if len(buses) > 1:
                for from_bus in buses:
                    for to_bus in buses:
                        if from_bus != to_bus:
                            to_bus_set = from_to_bus_edges.get(from_bus, set())
                            to_bus_set.add(to_bus)
                            from_to_bus_edges[from_bus] = to_bus_set
        source_bus_set = node_to_bus_map.get(source)
        target_bus_set = node_to_bus_map.get(target)
        if not source_bus_set or not target_bus_set:
            return -1
        if source == target:
            return 0
        queue = [(source_bus, 0) for source_bus in source_bus_set]
        visited = set()
        while queue:
            from_bus, curr_dist = queue.pop(0)
            visited.add(from_bus)
            curr_dist += 1
            if from_bus in target_bus_set:
                return curr_dist
            to_bus_set = from_to_bus_edges.get(from_bus, set())
            for to_bus in to_bus_set:
                if to_bus not in visited:
                    queue.append((to_bus, curr_dist))
            pass
        return -1


print(Solution().numBusesToDestination(routes=[[1, 2, 7], [3, 6, 7]],
                                       source=1,
                                       target=6))
print(Solution().numBusesToDestination(routes=[[7, 12], [4, 5, 15], [6],
                                               [15, 19], [9, 12, 13]],
                                       source=15,
                                       target=12))
