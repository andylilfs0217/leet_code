from enum import Enum
from io import TextIOWrapper


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    res = 0
    for line in lines:
        g1, g2 = [list(map(int, g.split('-'))) for g in line.split(',')]
        s1, s2 = set(range(g1[0], g1[1] + 1)), set(range(g2[0], g2[1] + 1))
        if s1 == s2 or s1.issubset(s2) or s2.issubset(s1):
            res += 1
        pass

    # Finish your codes here
    return res
