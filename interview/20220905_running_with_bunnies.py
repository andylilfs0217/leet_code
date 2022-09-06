"""
Running with Bunnies
====================

You and the bunny workers need to get out of this collapsing death trap of a space station -- and fast! Unfortunately, some of the bunnies have been weakened by their long work shifts and can't run very fast. Their friends are trying to help them, but this escape would go a lot faster if you also pitched in. The defensive bulkhead doors have begun to close, and if you don't make it through in time, you'll be trapped! You need to grab as many bunnies as you can and get through the bulkheads before they close. 

The time it takes to move from your starting point to all of the bunnies and to the bulkhead will be given to you in a square matrix of integers. Each row will tell you the time it takes to get to the start, first bunny, second bunny, ..., last bunny, and the bulkhead in that order. The order of the rows follows the same pattern (start, each bunny, bulkhead). The bunnies can jump into your arms, so picking them up is instantaneous, and arriving at the bulkhead at the same time as it seals still allows for a successful, if dramatic, escape. (Don't worry, any bunnies you don't pick up will be able to escape with you since they no longer have to carry the ones you did pick up.) You can revisit different spots if you wish, and moving to the bulkhead doesn't mean you have to immediately leave -- you can move to and from the bulkhead to pick up additional bunnies if time permits.

In addition to spending time traveling between bunnies, some paths interact with the space station's security checkpoints and add time back to the clock. Adding time to the clock will delay the closing of the bulkhead doors, and if the time goes back up to 0 or a positive number after the doors have already closed, it triggers the bulkhead to reopen. Therefore, it might be possible to walk in a circle and keep gaining time: that is, each time a path is traversed, the same amount of time is used or added.

Write a function of the form solution(times, time_limit) to calculate the most bunnies you can pick up and which bunnies they are, while still escaping through the bulkhead before the doors close for good. If there are multiple sets of bunnies of the same size, return the set of bunnies with the lowest worker IDs (as indexes) in sorted order. The bunnies are represented as a sorted list by worker ID, with the first bunny being 0. There are at most 5 bunnies, and time_limit is a non-negative integer that is at most 999.

For instance, in the case of
[
  [0, 2, 2, 2, -1],  # 0 = Start
  [9, 0, 2, 2, -1],  # 1 = Bunny 0
  [9, 3, 0, 2, -1],  # 2 = Bunny 1
  [9, 3, 2, 0, -1],  # 3 = Bunny 2
  [9, 3, 2, 2,  0],  # 4 = Bulkhead
]
and a time limit of 1, the five inner array rows designate the starting point, bunny 0, bunny 1, bunny 2, and the bulkhead door exit respectively. You could take the path:

Start End Delta Time Status
    -   0     -    1 Bulkhead initially open
    0   4    -1    2
    4   2     2    0
    2   4    -1    1
    4   3     2   -1 Bulkhead closes
    3   4    -1    0 Bulkhead reopens; you and the bunnies exit

With this solution, you would pick up bunnies 1 and 2. This is the best combination for this space station hallway, so the solution is [1, 2].

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution({{0, 1, 1, 1, 1}, {1, 0, 1, 1, 1}, {1, 1, 0, 1, 1}, {1, 1, 1, 0, 1}, {1, 1, 1, 1, 0}}, 3)
Output:
    [0, 1]

Input:
Solution.solution({{0, 2, 2, 2, -1}, {9, 0, 2, 2, -1}, {9, 3, 0, 2, -1}, {9, 3, 2, 0, -1}, {9, 3, 2, 2, 0}}, 1)
Output:
    [1, 2]

-- Python cases --
Input:
solution.solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
Output:
    [1, 2]

Input:
solution.solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)
Output:
    [0, 1]

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""


import heapq
import time
from typing import List


def solution(times, times_limit):
    start = time.time()
    res = solution1(times, times_limit)
    end = time.time()
    # print("Time used: ", "{:.5f}".format((end-start) * 10**3), "ms")
    return res


def bellmanFord(edges, start_node):
    """
    Bellman Ford algorithm. Take a square matrix [edges] and an int [start_node] to find out if there is a negative loop and the shortest path length from [start_node] to each node.
    """
    # Initialize
    n = len(edges)
    min_distances = [float('inf') if i != start_node else 0 for i in range(n)]

    # Find the shortest distance from [start_node] to each node
    for _ in range(n-1):
        for from_node, outs in enumerate(edges):
            for to_node, weight in enumerate(outs):
                if min_distances[from_node] + weight < min_distances[to_node]:
                    min_distances[to_node] = min_distances[from_node] + weight

    # Check if there are any negative loops
    has_negative_loop = False
    for from_node, outs in enumerate(edges):
        for to_node, weight in enumerate(outs):
            if min_distances[from_node] + weight < min_distances[to_node]:
                has_negative_loop = True
                break
        if has_negative_loop:
            break

    return has_negative_loop, min_distances


def reweightEdge(weight, from_node_val, to_node_val):
    """
    Calculate the new weight for the edge using the formula l(u,v) = w(u,v) + h(u) - h(v)
    """
    res = weight + from_node_val - to_node_val
    return res


def findShortestPaths(edges):
    """
    Find all shortest paths from one node to another node by providing a matrix of edges.
    """
    # Initialize
    n = len(edges)
    res = [[0 if i == j else float('inf')for i in range(n)] for j in range(n)]
    res[0][0] = 0

    # TODO: Implement dijkstra algorithm
    for start_node in range(n):
        distances = res[start_node]
        node_priority_queue = [(distances[node], node) for node in range(n)]
        heapq.heapify(node_priority_queue)
        while node_priority_queue:
            curr_dist, curr_node = heapq.heappop(node_priority_queue)
            for to_node in range(n):
                alt = distances[curr_node]
    return res


def solution1(times: List[List], times_limit):
    n = len(times)  # Number of stops
    total_bunnies = n - 2  # Number of total bunnies
    res = []  # response

    # Check if there is any bunnies
    if not total_bunnies:
        return res

    # Perform Bellman Ford algorithm with an additional node which only contains out-edges to each node.
    edges_for_bellman = list(times)
    edges_for_bellman = [[float('inf')] + row for row in edges_for_bellman]
    edges_for_bellman.insert(0, [0 for _ in range(n+1)])
    has_negative_loop, distances = bellmanFord(edges_for_bellman, 0)
    distances = distances[1:]  # Remove the additional node

    if has_negative_loop:
        # Having negative loop(s) means all bunnies can be retrieved before escaping.
        res = [i for i in range(total_bunnies)]
    else:
        # Reweight all edges to non-negative values
        new_times = list(times)
        for from_node, row in enumerate(new_times):
            for to_node, weight in enumerate(row):
                new_weight = reweightEdge(
                    weight, distances[from_node], distances[to_node])
                new_times[from_node][to_node] = new_weight
        # Find the shortest path from node U to node V
        shortest_paths = findShortestPaths(new_times)
        pass

    return res


print(solution([[0, 2, 2, 2, -1],
                [9, 0, 2, 2, -1],
                [9, 3, 0, 2, -1],
                [9, 3, 2, 0, -1],
                [9, 3, 2, 2, 0]], 1) == [1, 2])
print(solution([[0, 1, 1, 1, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0]], 3) == [0, 1])
print(solution([[0, 2, 2, 2, -1],
                [9, 0, 2, 2, 0],
                [9, 3, 0, 2, 0],
                [9, 3, 2, 0, 0],
                [-1, 3, 2, 2, 0]], 3) == [0, 1, 2])
print(solution([[1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1]], 1) == [])
print(solution([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]], 2) == [0])
print(solution([[0, 5, 11, 11, 1],
                [10, 0, 1, 5, 1],
                [10, 1, 0, 4, 0],
                [10, 1, 5, 0, 1],
                [10, 10, 10, 10, 0]], 10) == [0, 1])
print(solution([[0, 10, 10, 10, 1],
                [0, 0, 10, 10, 10],
                [0, 10, 0, 10, 10],
                [0, 10, 10, 0, 10],
                [1, 1, 1, 1, 0]], 5) == [0, 1])
print(solution([[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]], 1) == [0, 1, 2])
print(solution([[2, 2],
                [2, 2]], 1) == [])
print(solution([[0, 10, 10, 1, 10],
                [10, 0, 10, 10, 1],
                [10, 1, 0, 10, 10],
                [10, 10, 1, 0, 10],
                [1, 10, 10, 10, 0]], 6) == [0, 1, 2])
