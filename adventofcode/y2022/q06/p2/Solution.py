import collections
from enum import Enum
from io import TextIOWrapper


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    res = []
    MESSAGE_LEN = 14
    for line in lines:
        for r in range(MESSAGE_LEN, len(line) + 1):
            l = r - MESSAGE_LEN
            if len(set(line[l:r])) == MESSAGE_LEN:
                res.append(r)
                break

    # Finish your codes here
    return res
