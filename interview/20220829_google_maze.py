"""
question
Prepare the Bunnies' Escape
===========================
You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions.
You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1).
Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.
Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java
Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.


Python cases --

Input:
solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
Output:
7
Input:
solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [
                  0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
Output:
11


Java cases --

Input:
Solution.solution({{0, 1, 1, 0}, {0, 0, 0, 1}, {1, 1, 0, 0}, {1, 1, 1, 0}})
Output:
7
Input:
Solution.solution({{0, 0, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 0}, {0, 0, 0, 0, 0, 0}, {
                  0, 1, 1, 1, 1, 1}, {0, 1, 1, 1, 1, 1}, {0, 0, 0, 0, 0, 0}})
Output:
11
Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""


import heapq


class MinHeapQueue():
    def __init__(self) -> None:
        self.n = 0
        self.heap = []

    def isEmpty(self) -> bool:
        return self.n == 0

    def heappush(self, val):
        self.heap.append(val)
        self.n += 1
        i = self.n - 1
        while self.heap[i] > self.heap[(i-1)//2]:
            self.heap[i], self.heap[(
                i-1)//2] = self.heap[(i-1)//2], self.heap[i]

    def heappop(self):
        res = self.heap.pop(0)
        if self.n > 1:
            self.heap.insert(0, self.heap[-1])
            self.n -= 1
            i = 0
            while True:
                leftIdx, rightIdx = 2*i+1, 2*i+2
                if leftIdx >= self.n:
                    break
                maxIdx = leftIdx
                if rightIdx < self.n:
                    maxIdx = max(maxIdx, rightIdx)
                if self.heap[i] > self.heap[maxIdx]:
                    self.heap[i], self.heap[maxIdx] = self.heap[maxIdx], self.heap[i]
                else:
                    break
        return res


def solution(matrix) -> int:
    return solution1(matrix)


def solution1(matrix) -> int:
    m, n = len(matrix), len(matrix[0])
    DIRECTIONS = (
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    )

    def isOutOfBound(i: int, j: int) -> bool:
        return i < 0 or j < 0 or i >= m or j >= n

    def calHVal(i: int, j: int) -> int:
        return max(m-1-i, n-1-j)

    def printMatrix():
        for row in matrix:
            printRow = ''
            for cell in row:
                printRow += str(cell)
            print(printRow)

    # hVal, i, j, breakWallRemaining, step
    # pQueue = []
    # heapq.heappush(pQueue, (calHVal(0, 0), 1, 0, 0, 1))
    pQueue = MinHeapQueue()
    pQueue.heappush((calHVal(0, 0), 1, 0, 0, 1))
    while not pQueue.isEmpty():
        _, step, i, j, breakWallRemain = pQueue.heappop()
        # Reach the exit
        if i == m-1 and j == n-1:
            return step
        cell = matrix[i][j]
        # In the wall
        if cell == 1:
            breakWallRemain -= 1
        # No more breaking wall
        if breakWallRemain < 0:
            continue
        # Visited
        if cell == '*':
            continue
        # Change the current cell to visited
        matrix[i][j] = '*'
        for dirI, dirJ in DIRECTIONS:
            newI, newJ = i+dirI, j+dirJ
            if not isOutOfBound(newI, newJ):
                # heapq.heappush(pQueue, (calHVal(newI, newJ), step+1,
                #                         newI, newJ, breakWallRemain))
                pQueue.heappush((calHVal(newI, newJ), step+1,
                                newI, newJ, breakWallRemain))
    return


print(solution(
    [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution(
    [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) == 7)
print(solution(
    [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 11)
print(solution(
    [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 39)
