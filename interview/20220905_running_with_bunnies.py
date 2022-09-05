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


import time


def solution(times, times_limit):
    start = time.time()
    res = solution1(times, times_limit)
    end = time.time()
    print("Time used: ", "{:.5f}".format((end-start) * 10**3), "ms")
    return res


def solution1(times, times_limit):
    n = len(times)  # Number of stops
    total_bunnies = n - 2  # Number of total bunnies
    res = []  # response

    # Check if there is any bunnies
    if not total_bunnies:
        return res

    max_time_remain = [float('-inf') for _ in range(n)]
    max_time_remain[0] = times_limit
    # (time_remain, curr_idx, max_time_remain, visited_set, collected_bunnies)
    queue = [(times_limit, 0, max_time_remain, set(), set())]
    while queue:
        time_remain, curr_idx, max_time_remain, visited_set, collected_bunnies = queue.pop(
            0)
        # Can generate infinite time
        if curr_idx in visited_set and time_remain > max_time_remain[curr_idx]:
            res = [i for i in range(total_bunnies)]
            break
        # Arrive gateway
        if curr_idx == n-1 and time_remain >= 0:
            if len(collected_bunnies) <= len(res) and sorted(collected_bunnies) < res:
                res = sorted(collected_bunnies)
        max_time_remain[curr_idx] = max(max_time_remain[curr_idx], time_remain)
        visited_set.add(curr_idx)
        if curr_idx in range(1, n-1):
            collected_bunnies.add(curr_idx-1)
        # Append next possible steps
        for new_idx in range(n):
            new_time_remain = time_remain-times[curr_idx][new_idx]
            temp = (new_time_remain, new_idx, list(max_time_remain),
                    set(visited_set), set(collected_bunnies))
            queue.append(temp)
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
