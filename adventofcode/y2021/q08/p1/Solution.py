import collections
from io import TextIOWrapper
import math
import statistics
from typing import List


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    res = 0
    patterns, outputs = [], []
    for line in lines:
        a, b = line.split(' | ')
        a, b = a.split(), b.split()
        patterns.append(a)
        outputs.append(b)
    for output in outputs:
        for digit in output:
            if len(digit) in set([2, 3, 4, 7]):
                res += 1

    # Finish your codes here
    return res
