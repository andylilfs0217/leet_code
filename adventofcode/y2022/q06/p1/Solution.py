import collections
from enum import Enum
from io import TextIOWrapper


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    res = []
    for line in lines:
        for r in range(4, len(line) + 1):
            l = r - 4
            if len(set(line[l:r])) == 4:
                res.append(r)
                break

    # Finish your codes here
    return res
