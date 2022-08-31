"""
Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].

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
Solution.solution({{0, 2, 1, 0, 0}, {0, 0, 0, 3, 4}, {0, 0, 0, 0, 0}, {0, 0, 0, 0,0}, {0, 0, 0, 0, 0}})
Output:
    [7, 6, 8, 21]

Input:
Solution.solution({{0, 1, 0, 0, 0, 1}, {4, 0, 0, 3, 2, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})
Output:
    [0, 3, 2, 9, 14]

-- Python cases --
Input:
solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
Output:
    [7, 6, 8, 21]

Input:
solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
Output:
    [0, 3, 2, 9, 14]

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""


from fractions import Fraction
import numpy as np


def solution(m):
    """
    This question is a variant of Absorbing Markov Chain. Check out https://en.wikipedia.org/wiki/Absorbing_Markov_chain#Absorbing_probabilities for more.

    In short, we can turn the matrix into Canonical form:\\
    P = (
        Q R\\
        O I_r
    )\\
    t = number of transient states\\
    r = number of absorbing states\\
    Q = t*t matrix describing the probability of transitioning from some transient state to another\\
    R = r*t matrix describing the probability of transitioning from some transient state to some absorbing state\\
    O = t*r zero matrix\\
    I_r = r*r identity matrix

    And then we can turn it into a fundamental matrix\\
    N = (I_t - Q)^(-1)\\
    I_t = t*t identity matrix\\

    And finally we can calculate the probability to reach the absorbing state `j` from transient state `i`\\
    B = NR

    To get the result we want, we can simply convert `B[0]` into our desired format.
    """

    def transformToFracMatrix(m):
        """
        Transform original matrix into the matrix with fractions.
        """
        for i, row in enumerate(m):
            total = sum(row)
            if total:
                for j, cell in enumerate(row):
                    if cell:
                        m[i][j] = Fraction(cell, total)
        return m

    # def createIdentityMatrix(n):
    #     """
    #     Create a n*n identity matrix
    #     """
    #     matrix = []
    #     for i in range(n):
    #         row = []
    #         for j in range(n):
    #             row.append(1 if i == j else 0)
    #         matrix.append(row)
    #     return matrix

    def getMatrixQ(m, tIdxs):
        """
        Create matrix Q.

        Q = t*t matrix describing the probability of transitioning from some transient state to another
        """
        matrixQ = []
        for i in tIdxs:
            row = m[i]
            rowQ = []
            for j in tIdxs:
                prob = row[j]
                rowQ.append(prob)
            matrixQ.append(rowQ)
        return np.array(matrixQ)

    def getMatrixN(t, matrixQ):
        """
        Create matrix N.

        N = (I_t - Q)^(-1)
        """
        # matrixIdentity = createIdentityMatrix(t)
        matrixIdentity = np.identity(t)
        matrixNInverse = np.subtract(matrixIdentity, matrixQ)
        matrixNInverse = matrixNInverse.astype('float64')
        matrixN = np.linalg.inv(matrixNInverse)
        matrixN = matrixN + Fraction()
        return matrixN

    def getMatrixR(m, tIdxs, aIdxs):
        """
        Create matrix R.

        R = r*t matrix describing the probability of transitioning from some transient state to some absorbing state
        """
        matrixR = []
        for i in tIdxs:
            row = m[i]
            rowR = []
            for j in aIdxs:
                prob = row[j]
                rowR.append(prob)
            matrixR.append(rowR)
        matrixR = np.array(matrixR)
        matrixR = matrixR.transpose()
        return matrixR

    def getMatrixB(matrixN, matrixR):
        """
        Create matrix B.

        B = NR
        """
        return

    def getRes(matrixB):
        """
        Return desired result of the question.

        An array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form.
        """
        return

    # Transform matrix into fraction matrix for easier calculation
    m = transformToFracMatrix(m)

    # Get transient states and absorbing states
    transientStateIdxs, absorbingStateIdxs = [], []
    for i, row in enumerate(m):
        (transientStateIdxs if sum(row) else absorbingStateIdxs).append(i)

    m = np.array(m)

    # Get different matrixes for calculation
    matrixQ = getMatrixQ(m, transientStateIdxs)
    matrixN = getMatrixN(len(transientStateIdxs), matrixQ)
    matrixR = getMatrixR(m, transientStateIdxs, absorbingStateIdxs)
    matrixB = getMatrixB(matrixN, matrixR)

    # Get the desired result
    res = getRes(matrixB)
    return res


# print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [
#       0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == [7, 6, 8, 21])
print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [
      0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == [0, 3, 2, 9, 14])
