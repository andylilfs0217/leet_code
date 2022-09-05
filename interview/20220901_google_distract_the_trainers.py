"""
Distract the Trainers
=====================

The time for the mass escape has come, and you need to distract the bunny trainers so that the workers can make it out! Unfortunately for you, they're watching the bunnies closely. Fortunately, this means they haven't realized yet that the space station is about to explode due to the destruction of the LAMBCHOP doomsday device. Also fortunately, all that time you spent working as first a minion and then a henchman means that you know the trainers are fond of bananas. And gambling. And thumb wrestling.

The bunny trainers, being bored, readily accept your suggestion to play the Banana Games.

You will set up simultaneous thumb wrestling matches. In each match, two trainers will pair off to thumb wrestle. The trainer with fewer bananas will bet all their bananas, and the other trainer will match the bet. The winner will receive all of the bet bananas. You don't pair off trainers with the same number of bananas (you will see why, shortly). You know enough trainer psychology to know that the one who has more bananas always gets over-confident and loses. Once a match begins, the pair of trainers will continue to thumb wrestle and exchange bananas, until both of them have the same number of bananas. Once that happens, both of them will lose interest and go back to supervising the bunny workers, and you don't want THAT to happen!

For example, if the two trainers that were paired started with 3 and 5 bananas, after the first round of thumb wrestling they will have 6 and 2 (the one with 3 bananas wins and gets 3 bananas from the loser). After the second round, they will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they stop and get back to training bunnies.

How is all this useful to distract the bunny trainers? Notice that if the trainers had started with 1 and 4 bananas, then they keep thumb wrestling! 1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.

Now your plan is clear. You must pair up the trainers in such a way that the maximum number of trainers go into an infinite thumb wrestling loop!

Write a function solution(banana_list) which, given a list of positive integers depicting the amount of bananas the each trainer starts with, returns the fewest possible number of bunny trainers that will be left to watch the workers. Element i of the list will be the number of bananas that trainer i (counting from 0) starts with.

The number of trainers will be at least 1 and not more than 100, and the number of bananas each trainer starts with will be a positive integer no more than 1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(1,1)
Output:
    2

Input:
solution.solution([1, 7, 3, 21, 13, 19])
Output:
    0

-- Java cases --
Input:
solution.solution(1,1)
Output:
    2

Input:
Solution.solution([1, 7, 3, 21, 13, 19])
Output:
    0

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""


def checkInfinite(a, b, totalToMinNumDivBy2):
    total = a+b
    if total in totalToMinNumDivBy2:
        minNumDivBy2 = totalToMinNumDivBy2[total]
    else:
        minNumDivBy2 = total
        while minNumDivBy2 % 2 == 0:
            minNumDivBy2 //= 2
        totalToMinNumDivBy2[total] = minNumDivBy2
    return a % minNumDivBy2 != 0, totalToMinNumDivBy2


def solution(banana_list):
    totalToMinNumDivBy2 = {}
    n = len(banana_list)
    pairMap = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            a, b = banana_list[i], banana_list[j]
            isInf, totalToMinNumDivBy2 = checkInfinite(
                a, b, totalToMinNumDivBy2)
            if isInf:
                pairMap[i][j], pairMap[j][i] = 1, 1
    toBeProcessed = n
    visitedIdx = set()
    res = 0
    while toBeProcessed > 0:
        # Find the index with the minimum number of pairables
        i = 0
        while i < n and i in visitedIdx:
            i += 1
        minPairableIdx = i
        for i in range(n):
            minPairableRow, row = pairMap[minPairableIdx], pairMap[i]
            if i not in visitedIdx and sum(row) < sum(minPairableRow):
                minPairableIdx = i
        minNumPairables = sum(minPairableRow)
        # Remove pair/single
        if minNumPairables == 0:
            for i in range(n):
                pairMap[i][minPairableIdx] = 0
                pairMap[minNumPairables][i] = 0
            visitedIdx.add(minPairableIdx)
            toBeProcessed -= 1
            res += 1
        else:
            pairIdx = minPairableRow.index(1)
            for i in range(n):
                cell = minPairableRow[i]
                if cell and sum(pairMap[i]) < sum(pairMap[pairIdx]):
                    pairIdx = i
            if sum(pairMap[pairIdx]) > 0:
                for i in range(n):
                    pairMap[i][minPairableIdx] = 0
                    pairMap[minPairableIdx][i] = 0
                    pairMap[i][pairIdx] = 0
                    pairMap[pairIdx][i] = 0
                visitedIdx.add(minPairableIdx)
                visitedIdx.add(pairIdx)
                toBeProcessed -= 2
    return res


print(solution([1, 1]) == 2)
print(solution([1, 7, 3, 21, 13, 19]) == 0)
